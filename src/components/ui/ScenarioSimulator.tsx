"use client";

import { useState } from "react";

interface ScenarioSimulatorProps {
    city: string;
    lat: number;
    lon: number;
}

export default function ScenarioSimulator({ city, lat, lon }: ScenarioSimulatorProps) {
    const [rainfall, setRainfall] = useState(0);
    const [temperature, setTemperature] = useState(28);
    const [drainage, setDrainage] = useState(50);
    const [result, setResult] = useState<{ flood_risk_index: number; heat_risk_index: number; compound_risk_index: number } | null>(null);
    const [status, setStatus] = useState("");

    const simulate = async () => {
        setStatus("Calculating scenario...");
        try {
            const response = await fetch("http://127.0.0.1:8001/scenario", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    city,
                    lat,
                    lon,
                    rainfall_mm: rainfall,
                    temperature_c: temperature,
                    drainage_capacity_index: drainage,
                }),
            });
            if (!response.ok) throw new Error("Scenario unavailable");
            const payload = await response.json();
            setResult(payload.scenario);
            setStatus("Simulated scenario; not an official forecast.");
        } catch {
            setStatus("Scenario service unavailable");
        }
    };

    return (
        <section className="civic-card">
            <div className="flex justify-between items-start border-b border-[var(--color-navy)]/10 pb-3">
                <div>
                    <h2 className="text-xl m-0 font-black uppercase tracking-tight">What-If Simulator</h2>
                    <p className="text-[10px] text-[#59616b] uppercase tracking-widest mt-1">Scenario model only</p>
                </div>
                <button type="button" onClick={() => { setRainfall(0); setTemperature(28); setDrainage(50); setResult(null); setStatus(""); }} className="text-[9px] font-black uppercase text-[var(--color-navy)]">Reset</button>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 mt-4">
                <label className="text-[9px] font-black uppercase text-[#59616b]">Rainfall mm<input className="w-full" type="range" min="0" max="300" value={rainfall} onChange={(event) => setRainfall(Number(event.target.value))} /><span className="text-[var(--color-navy)]">{rainfall}</span></label>
                <label className="text-[9px] font-black uppercase text-[#59616b]">Temperature °C<input className="w-full" type="range" min="15" max="50" value={temperature} onChange={(event) => setTemperature(Number(event.target.value))} /><span className="text-[var(--color-navy)]">{temperature}</span></label>
                <label className="text-[9px] font-black uppercase text-[#59616b]">Drainage efficiency<input className="w-full" type="range" min="0" max="100" value={drainage} onChange={(event) => setDrainage(Number(event.target.value))} /><span className="text-[var(--color-navy)]">{drainage}%</span></label>
            </div>
            <button type="button" onClick={simulate} className="civic-button mt-4 text-xs">Run Scenario</button>
            {result && <div className="grid grid-cols-3 gap-2 mt-4 text-center"><div><b className="block text-lg text-[var(--color-navy)]">{result.flood_risk_index}</b><span className="text-[9px] uppercase text-[#59616b]">Flood</span></div><div><b className="block text-lg text-[var(--color-navy)]">{result.heat_risk_index}</b><span className="text-[9px] uppercase text-[#59616b]">Heat</span></div><div><b className="block text-lg text-[var(--color-navy)]">{result.compound_risk_index}</b><span className="text-[9px] uppercase text-[#59616b]">Compound</span></div></div>}
            {status && <p className="text-[10px] font-bold text-[#59616b] uppercase mt-3">{status}</p>}
        </section>
    );
}
