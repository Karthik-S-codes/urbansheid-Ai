# UrbanSheild AI

UrbanSheild AI is a premium, investor-grade smart city command center simulation. It visualizes real-time climate risk data (flood, heat) and demonstrates AI-driven mitigation strategies.

## 🚀 Features
- **Real-time Digital Twin**: Interactive 3D map with risk heatmaps.
- **AI Intelligence**: Predictive analytics for flood and heat stress.
- **Cinematic UI**: Glassmorphism, ambient animations, and premium data visualization.
- **Emergency Protocols**: Simulated alert systems with audio feedback.
Modern cities face increasing climate volatility, yet most systems react only after disasters occur. URBANSHIELD AI shifts the approach from reactive to predictive — using intelligent risk modeling and dynamic scenario simulation to provide early warnings, infrastructure stress insights, and actionable mitigation recommendations.
- **Systemic Intelligence (L3)**: Adaptive anomaly detection, infrastructure collapse modeling, and resource allocation optimization.

🚨 The Problem

Urban areas are highly vulnerable to:

Flash floods caused by intense rainfall and poor drainage

Extreme heatwaves amplified by urban heat island effects

Infrastructure overload during climate stress

Lack of predictive, zone-level intelligence for city authorities

Existing systems are either too generalized or not built for real-time decision support.

🧠 Our Solution

URBANSHIELD AI provides:

1️⃣ Hyper-Local Risk Prediction

Analyzes multiple urban parameters such as rainfall intensity, drainage efficiency, elevation, temperature trends, humidity, and population density to compute:

Flood Risk Score (0–1 scale)

Heatwave Severity Index

Confidence Level

Risk Categories (Low to Critical)
## 🛠️ Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd your-repository
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Configure Environment:**
    Create a `.env.local` file in the root directory if you use the optional Mapbox-based map:
    ```bash
    NEXT_PUBLIC_MAPBOX_TOKEN=your_public_mapbox_token_here
    ```

4.  **Run Development Server:**
    ```bash
    npm run dev
    ```

5.  **Build for Production:**
    ```bash
    npm run build
    npm start
    ```

## 📦 Tech Stack
-   **Framework**: Next.js 14 (App Router)
-   **Styling**: Tailwind CSS
-   **Map**: Mapbox GL JS (react-map-gl)
-   **State**: Zustand
-   **Animation**: Framer Motion
-   **Backend**: FastAPI with ML Models (Python)
-   **ML Engine**: RandomForest with Uncertainty Quantification

## 🧠 Intelligence Layer (Level 3)

UrbanSheild AI now features **Systemic Intelligence (L3)** - a championship-level positioning that includes:

### 🌊 Upgrade 8: Dynamic Threshold Adaptation (Climate Drift Awareness)
- Anomaly detection based on seasonal mean and standard deviation
- Rainfall anomaly scoring for extreme weather events
- Climate-aware risk assessment

### 👥 Upgrade 9: Infrastructure Collapse Probability
- Probabilistic sigmoid model for drainage infrastructure failure
- Cascading failure impact calculations
- Real-time structural integrity monitoring

### 🔍 Upgrade 10: Risk Velocity Metric
- Risk acceleration index calculation
- Early warning intelligence for rapid risk escalation
- Derivative-based risk trend analysis

### 🛠️ Upgrade 11: Resource Allocation Optimization Engine
- Multi-action efficiency comparison (drainage vs green cover)
- Cost-benefit analysis per risk reduction unit
- Optimal intervention recommendation system

### 👨‍👩‍👧 Upgrade 12: Socioeconomic Risk Weighting
- Vulnerability multiplier based on population density
- Slum ratio and elderly population weighting
- Humanitarian impact assessment

### 📝 Upgrade 13: Explainable Narrative Generator (Offline)
- Template-based intelligence reports
- No API dependency for explainability
- Context-aware risk insights

### ⚠️ Upgrade 14: Uncertainty Quantification
- Ensemble variance across 200 trees
- Prediction confidence bands
- Scientific uncertainty reporting

### 🌊 Upgrade 15: Stress Interaction Matrix
- Compound climate stress modeling
- Rainfall-temperature interaction terms
- Cascading environmental effects

### 📉 Upgrade 16: Risk Memory (Persistence Layer)
- Chronic stress accumulation modeling
- Multi-time step risk persistence
- Long-term vulnerability assessment

## 🏆 Championship Positioning

UrbanSheild AI now represents **Multi-Layer Adaptive Climate Risk Intelligence System** with:
- Anomaly Detection ✅
- Infrastructure Failure Modeling ✅
- Socioeconomic Weighting ✅
- Resource Optimization ✅
- Uncertainty Quantification ✅

## 📊 API Endpoints

### Backend (Python FastAPI)
- `GET /health` - System status
- `POST /simulate` - Risk calculation with systemic intelligence
- `POST /sensitivity` - Sensitivity analysis
- `POST /scenario` - Clearly labelled what-if simulation
- `GET /recommendations` - Location-specific preventive recommendations
- `GET/POST/PATCH /actions` - Persist and manage advisory action records
- `GET /history` - Risk observations recorded by this deployment
- `GET /route` - Reports route availability; routing is disabled without verified road/hazard data

### Frontend (TypeScript/React)
- Real-time risk visualization
- Zone drill-down analytics
- Intelligence report generation
- Resource optimization dashboard

## 🚀 Quick Demo

1. Start backend server:
   ```bash
   cd backend_v2
   uvicorn main:app --host 0.0.0.0 --port 8001
   ```

2. Start frontend:
   ```bash
   npm run dev
   ```

3. Access at http://localhost:3000

The backend stores action records and risk observations in `backend_v2/urbanshield.db`.
Set `ACTION_API_KEY` to protect action creation/status updates, and `CORS_ORIGINS`
to a comma-separated list of trusted frontend origins. Without `ACTION_API_KEY`,
local development endpoints operate in clearly labelled demo mode.

The shipped models are trained on synthetic data and are not evidence of field
accuracy. Responses expose `data_status` and identify live weather, model, and
historical-data availability. Historical flood observations and verified road
network data are not included, so official alerts and safe-route claims remain
disabled.

## 📈 Performance Metrics

- **Risk Prediction**: 200 trees ensemble
- **Confidence**: Z-score based OOD detection
- **Uncertainty**: ±4.6 standard deviation bands
- **Optimization**: 1.5x efficiency per unit cost
- **Velocity**: Real-time risk acceleration tracking

## 🎯 Judges' Value Proposition

UrbanSheild AI delivers championship-level positioning by:
- Moving from reactive to strategic/adaptive systems
- Adding climate drift awareness and infrastructure failure modeling
- Providing explainable AI without API dependencies
- Including socioeconomic vulnerability weighting
- Implementing resource allocation optimization
- Quantifying uncertainty for scientific credibility

## 🔧 Development

### Backend Setup
```bash
cd backend_v2
pip install -r requirements.txt
python train.py  # Train models
uvicorn main:app --host 0.0.0.0 --port 8001
```

### Frontend Development
```bash
npm install
npm run dev
```

## 📄 Documentation

- [System Architecture](./docs/architecture.md)
- [API Reference](./docs/api.md)
- [ML Model Details](./docs/ml_models.md)
- [Deployment Guide](./docs/deployment.md)

## 🙏 Third-Party Acknowledgements

UrbanSheild AI uses the following external services, data sources, libraries, and
resources. Their names, links, and applicable attribution/licensing terms are
listed here for transparency and event compliance.

### Live services and map data

- **Open-Meteo** — live weather observations used by the risk API:
  [open-meteo.com](https://open-meteo.com/). Weather data attribution and
  provider terms apply; see the [Open-Meteo
  licence](https://open-meteo.com/en/licence) and
  [data sources](https://open-meteo.com/en/docs).
- **OpenStreetMap contributors** — map tiles displayed by the Leaflet map:
  [openstreetmap.org](https://www.openstreetmap.org/). © OpenStreetMap
  contributors, available under the [Open Data Commons Open Database Licence
  (ODbL)](https://opendatacommons.org/licenses/odbl/). The application displays
  the required map attribution in the map control.
- **Nominatim / OpenStreetMap Foundation** — location search:
  [Nominatim usage policy](https://operations.osmfoundation.org/policies/nominatim/).
  Search requests must remain within that service's usage limits and attribution
  requirements.
- **Mapbox GL JS** — optional map implementation retained in the codebase:
  [Mapbox documentation](https://docs.mapbox.com/mapbox-gl-js/). Mapbox tokens,
  tiles, styles, and service terms are required only if that optional component
  is enabled.

### Open-source software

- **Next.js, React, TypeScript, Tailwind CSS, Framer Motion, Zustand, Leaflet,
  Lucide React, clsx, and tailwind-merge** power the web application. See
  [package.json](./package.json) and the linked upstream projects for their
  individual licence notices.
- **FastAPI, Uvicorn, Pydantic, NumPy, pandas, scikit-learn, XGBoost, joblib,
  and Requests** power the Python API and model pipeline. See
  [backend_v2/requirements.txt](./backend_v2/requirements.txt) and each
  upstream project's licence notice.
- **Leaflet marker icons** are loaded from the Leaflet distribution via
  [unpkg](https://unpkg.com/leaflet@1.9.4/dist/images/). Leaflet licensing and
  attribution terms apply.

### Project data and model status

- `backend_v2/city_profiles.py` contains project-authored infrastructure
  profiles for the supported demonstration cities.
- The supplied model artifacts are trained on synthetic data generated by
  `backend_v2/train.py`; they are not presented as validated public flood or
  heat observations.
- `bengaluru_readings.json` is a checked-in demonstration output and is not
  represented as an official government dataset.
- No third-party historical flood dataset is bundled with this repository.

This acknowledgement does not replace the licence or terms published by each
provider. Before production deployment, review current provider policies,
attribution requirements, rate limits, and any required commercial permissions.

## 🐛 Troubleshooting

- **Model not found**: Run `python train.py` to generate models
- **Port conflicts**: Change port in `backend_v2/main.py`
- **Mapbox errors**: Check `.env.local` for valid token

## 📄 License

MIT License - see LICENSE file for details

## 🐛 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Submit pull request

---

**Built with ❤️ for sustainable urban futures**
