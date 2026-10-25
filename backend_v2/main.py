from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Header
from pydantic import BaseModel, Field
from typing import Any, Optional
from datetime import datetime, timezone
import json
import os
import sqlite3
import uvicorn
from risk_engine import UrbanRiskEngine
from city_profiles import CITIES
from weather_service import weather_service as ws

app = FastAPI(title="UrbanShield Deep Intelligence Engine v2.5")
engine = UrbanRiskEngine()
DATABASE_PATH = os.path.join(os.path.dirname(__file__), "urbanshield.db")

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "http://localhost:3000").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SimulationInputs(BaseModel):
    rainfall_mm: float
    avg_temperature_c: float
    humidity_percent: float
    drainage_capacity_index: float # 0-100
    green_cover_percent: float # 0-100
    population_density: float
    elevation_index: Optional[float] = 50.0
    infrastructure_strength: Optional[float] = 70.0
    emergency_response: Optional[float] = 80.0


class ScenarioRequest(BaseModel):
    city: str = "Bengaluru"
    lat: float = Field(12.9716, ge=-90, le=90)
    lon: float = Field(77.5946, ge=-180, le=180)
    rainfall_mm: Optional[float] = Field(None, ge=0, le=1000)
    temperature_c: Optional[float] = Field(None, ge=-50, le=70)
    humidity_percent: Optional[float] = Field(None, ge=0, le=100)
    drainage_capacity_index: Optional[float] = Field(None, ge=0, le=100)


class ActionCreate(BaseModel):
    location: str
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    risk_type: str
    priority: str
    reason: str
    responsible_department: str


class ActionStatusUpdate(BaseModel):
    status: str


def _db() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS actions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            risk_type TEXT NOT NULL,
            priority TEXT NOT NULL,
            reason TEXT NOT NULL,
            responsible_department TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending',
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS risk_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            flood_risk REAL NOT NULL,
            heat_risk REAL NOT NULL,
            compound_risk REAL NOT NULL,
            source TEXT NOT NULL,
            observed_at TEXT NOT NULL
        )
        """
    )
    connection.commit()
    return connection


def _recommendations(result: dict[str, Any], location: str, lat: float, lon: float) -> list[dict[str, Any]]:
    recommendations = []
    flood = float(result["flood_risk_index"])
    heat = float(result["heat_risk_index"])
    if flood >= 35:
        priority = "Critical" if flood >= 75 else "High" if flood >= 55 else "Medium"
        recommendations.append({
            "location": location,
            "latitude": lat,
            "longitude": lon,
            "risk_type": "Flood",
            "priority": priority,
            "reason": f"Flood risk index is {flood:.1f}; inspect drainage and monitor vulnerable road segments.",
            "responsible_department": "Drainage & Roads",
            "status": "Pending",
        })
    if heat >= 35:
        priority = "Critical" if heat >= 75 else "High" if heat >= 55 else "Medium"
        recommendations.append({
            "location": location,
            "latitude": lat,
            "longitude": lon,
            "risk_type": "Heat",
            "priority": priority,
            "reason": f"Heat risk index is {heat:.1f}; assess shade, hydration, and cooling-shelter coverage.",
            "responsible_department": "Public Health & Resilience",
            "status": "Pending",
        })
    if not recommendations:
        recommendations.append({
            "location": location,
            "latitude": lat,
            "longitude": lon,
            "risk_type": "Monitoring",
            "priority": "Low",
            "reason": "Current indices are below the preventive-action threshold; continue monitoring.",
            "responsible_department": "City Operations",
            "status": "Pending",
        })
    return recommendations


def _record_history(location: str, lat: float, lon: float, result: dict[str, Any], source: str) -> None:
    now = datetime.now(timezone.utc).isoformat()
    with _db() as connection:
        connection.execute(
            "INSERT INTO risk_history (location, latitude, longitude, flood_risk, heat_risk, compound_risk, source, observed_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (location, lat, lon, result["flood_risk_index"], result["heat_risk_index"], result["compound_risk_index"], source, now),
        )
        connection.commit()


def _calculate_for_location(city_key: str, overrides: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    city = CITIES.get(city_key)
    if city is None:
        city = {
            "name": city_key,
            "lat": float(overrides.get("lat", 20.5937)),
            "lon": float(overrides.get("lon", 78.9629)),
            "drainage_capacity_index": 50,
            "elevation_index": 50,
            "population_density": 5000,
            "green_cover_percent": 20,
            "infrastructure_strength": 70,
            "emergency_response": 75,
        }
    target_lat = float(overrides.get("lat", city["lat"]))
    target_lon = float(overrides.get("lon", city["lon"]))
    cache_key = f"{city_key}_{target_lat}_{target_lon}"
    weather = ws.fetch_live_weather(target_lat, target_lon, cache_key)
    engine_inputs = {
        **city,
        **weather,
        **{key: float(value) for key, value in overrides.items() if value is not None and key not in ("lat", "lon")},
    }
    result = engine.calculate_risk(engine_inputs)
    result["data_status"] = {
        "mode": "live-weather-plus-validated-local-model",
        "weather_source": "Open-Meteo",
        "model_status": "loaded",
        "historical_flood_data": "not-configured",
        "is_forecast": False,
        "timestamp": weather["timestamp"],
    }
    result["input_snapshot"] = {
        "rainfall_mm": engine_inputs["rainfall_mm"],
        "avg_temperature_c": engine_inputs["avg_temperature_c"],
        "humidity_percent": engine_inputs["humidity_percent"],
        "drainage_capacity_index": engine_inputs["drainage_capacity_index"],
        "green_cover_percent": engine_inputs["green_cover_percent"],
        "population_density": engine_inputs["population_density"],
        "elevation_index": engine_inputs["elevation_index"],
    }
    result["contributing_factors"] = [
        {"name": "Rainfall", "value": engine_inputs["rainfall_mm"], "unit": "mm"},
        {"name": "Temperature", "value": engine_inputs["avg_temperature_c"], "unit": "°C"},
        {"name": "Drainage capacity", "value": engine_inputs["drainage_capacity_index"], "unit": "%"},
        {"name": "Elevation index", "value": engine_inputs["elevation_index"], "unit": "0-100"},
    ]
    result["recommendations"] = _recommendations(result, city_key, target_lat, target_lon)
    result["location"] = {"name": city_key, "lat": target_lat, "lon": target_lon}
    return result, weather

@app.get("/health")
async def health_check():
    return {
        "status": "online", 
        "version": "2.5.0-DEEP-INTEL", 
        "engine": "Hybrid-ML-Optimization",
        "model_status": "loaded",
        "database": "sqlite",
    }

@app.post("/simulate")
async def simulate_risk(inputs: SimulationInputs):
    try:
        data = inputs.dict()
        result = engine.calculate_risk(data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/sensitivity")
async def analyze_sensitivity(inputs: SimulationInputs):
    """
    Upgrade 5: Sensitivity Analysis for systemic volatility.
    """
    try:
        data = inputs.dict()
        sensitivity_report = engine.analyze_sensitivity(data)
        return sensitivity_report
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze-city")
async def analyze_city(payload: dict):
    """
    Phase 3: Real-time City Analysis Endpoint.
    Fetches live weather and merges with city infrastructure profiles.
    """
    city_key = payload.get("city", "Bengaluru")
    try:
        results, weather = _calculate_for_location(city_key, payload.get("overrides", {}))
        target_lat = results["location"]["lat"]
        target_lon = results["location"]["lon"]
        # 4. Add metadata for Frontend
        results["city_metadata"] = {
            "name": city_key,
            "lat": target_lat,
            "lon": target_lon,
            "data_source": "Open-Meteo + UrbanShield Profiles",
            "last_updated": weather["timestamp"],
            "is_live_sync": True
        }
        results["live_weather"] = weather
        _record_history(city_key, target_lat, target_lon, results, "live-weather-plus-validated-local-model")
        return results
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Intelligence Error: {str(e)}")


@app.post("/scenario")
async def scenario(request: ScenarioRequest):
    overrides = {
        "lat": request.lat,
        "lon": request.lon,
        **({"rainfall_mm": request.rainfall_mm} if request.rainfall_mm is not None else {}),
        **({"avg_temperature_c": request.temperature_c} if request.temperature_c is not None else {}),
        **({"humidity_percent": request.humidity_percent} if request.humidity_percent is not None else {}),
        **({"drainage_capacity_index": request.drainage_capacity_index} if request.drainage_capacity_index is not None else {}),
    }
    result, _ = _calculate_for_location(request.city, overrides)
    result["data_status"]["mode"] = "scenario-model-with-live-baseline"
    result["data_status"]["is_forecast"] = False
    return {"scenario": result, "label": "Simulated scenario; not an official forecast."}


@app.get("/recommendations")
async def recommendations(city: str = "Bengaluru", lat: float = 12.9716, lon: float = 77.5946):
    result, _ = _calculate_for_location(city, {"lat": lat, "lon": lon})
    return {"location": result["location"], "recommendations": result["recommendations"], "data_status": result["data_status"]}


@app.get("/actions")
async def list_actions(status: Optional[str] = None):
    with _db() as connection:
        query = "SELECT * FROM actions"
        params: tuple[str, ...] = ()
        if status:
            query += " WHERE status = ?"
            params = (status,)
        query += " ORDER BY created_at DESC"
        return {"actions": [dict(row) for row in connection.execute(query, params).fetchall()]}


@app.post("/actions")
async def create_action(action: ActionCreate, x_action_api_key: Optional[str] = Header(None)):
    configured_key = os.getenv("ACTION_API_KEY")
    if configured_key and x_action_api_key != configured_key:
        raise HTTPException(status_code=401, detail="Authorized action API key required")
    now = datetime.now(timezone.utc).isoformat()
    with _db() as connection:
        cursor = connection.execute(
            "INSERT INTO actions (location, latitude, longitude, risk_type, priority, reason, responsible_department, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, 'Pending', ?, ?)",
            (action.location, action.latitude, action.longitude, action.risk_type, action.priority, action.reason, action.responsible_department, now, now),
        )
        connection.commit()
        return {"action": dict(connection.execute("SELECT * FROM actions WHERE id = ?", (cursor.lastrowid,)).fetchone())}


@app.patch("/actions/{action_id}")
async def update_action(action_id: int, update: ActionStatusUpdate, x_action_api_key: Optional[str] = Header(None)):
    allowed = {"Pending", "Approved", "In Progress", "Completed", "Rejected"}
    if update.status not in allowed:
        raise HTTPException(status_code=400, detail=f"Status must be one of: {', '.join(sorted(allowed))}")
    configured_key = os.getenv("ACTION_API_KEY")
    if configured_key and x_action_api_key != configured_key:
        raise HTTPException(status_code=401, detail="Authorized action API key required")
    now = datetime.now(timezone.utc).isoformat()
    with _db() as connection:
        cursor = connection.execute("UPDATE actions SET status = ?, updated_at = ? WHERE id = ?", (update.status, now, action_id))
        connection.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Action not found")
        return {"action": dict(connection.execute("SELECT * FROM actions WHERE id = ?", (action_id,)).fetchone())}


@app.get("/history")
async def history(city: Optional[str] = None, limit: int = 50):
    bounded_limit = min(max(limit, 1), 200)
    with _db() as connection:
        if city:
            rows = connection.execute("SELECT * FROM risk_history WHERE location = ? ORDER BY observed_at DESC LIMIT ?", (city, bounded_limit)).fetchall()
        else:
            rows = connection.execute("SELECT * FROM risk_history ORDER BY observed_at DESC LIMIT ?", (bounded_limit,)).fetchall()
        return {"history": [dict(row) for row in rows], "data_status": "historical observations recorded by this deployment"}


@app.get("/route")
async def route():
    return {
        "available": False,
        "status": "unavailable",
        "message": "Routing is not enabled because no road-network and confirmed hazard data source is configured.",
        "warning": "A low model risk score must not be interpreted as a safe route.",
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
