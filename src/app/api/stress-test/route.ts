import { NextResponse } from "next/server";
import { logger } from "@/utils/logger";
import { ApiResponse } from "@/types";
import { weatherService } from "@/services/weatherService";

export async function POST(req: Request): Promise<NextResponse<ApiResponse>> {
    try {
        const text = await req.text();
        if (!text) {
            return NextResponse.json({
                success: false,
                error: "Empty request body",
                code: "VALIDATION_ERROR"
            }, { status: 400 });
        }

        const body = JSON.parse(text);

        // Request Validation
        if (body.lat !== undefined && typeof body.lat !== 'number') {
            return NextResponse.json({ success: false, error: "Invalid latitude", code: "VALIDATION_ERROR" }, { status: 400 });
        }
        const lonValid = typeof body.lng === 'number' || typeof body.lon === 'number' || (body.lng === undefined && body.lon === undefined);
        if (!lonValid) {
            return NextResponse.json({ success: false, error: "Invalid longitude", code: "VALIDATION_ERROR" }, { status: 400 });
        }

        let cityStr = body.city || "Bengaluru";
        const lat = body.lat;
        const lon = body.lng || body.lon;

        logger.info(`Processing stress-test for ${cityStr} (${lat}, ${lon})`);

        // Fetch real-time weather telemetry
        const weather = await weatherService.fetchWeather(Number(lat), Number(lon));

        // Forward to Python hybrid engine with real weather overrides
        const response = await fetch("http://127.0.0.1:8001/analyze-city", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                city: cityStr,
                overrides: {
                    ...(lat !== undefined && { lat: Number(lat) }),
                    ...(lon !== undefined && { lon: Number(lon) }),
                    ...(weather && {
                        avg_temperature_c: weather.temperature,
                        humidity_percent: weather.humidity,
                        rainfall_mm: weather.rainfall,
                        windspeed: weather.windspeed
                    })
                }
            })
        });

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`Python Engine Error: ${response.status} ${errorText}`);
        }

        const data = await response.json();

        return NextResponse.json({
            success: true,
            data,
            timestamp: new Date().toISOString(),
            source: "urban-intelligence-core"
        });

    } catch (error: any) {
        logger.error("API error in stress-test route", error.message);
        return NextResponse.json(
            { success: false, error: "Computation failed", code: "API_ERROR" },
            { status: 500 }
        );
    }
}
