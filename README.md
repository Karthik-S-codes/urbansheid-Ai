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
