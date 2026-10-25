"use client";

import { useState } from "react";

interface Recommendation {
    location: string;
    latitude: number;
    longitude: number;
    risk_type: string;
    priority: string;
    reason: string;
    responsible_department: string;
    status: string;
}

interface RecommendedActionsProps {
    recommendations: Recommendation[];
}

export default function RecommendedActions({ recommendations }: RecommendedActionsProps) {
    const [saved, setSaved] = useState<Record<number, string>>({});
    const [saving, setSaving] = useState<number | null>(null);

    const saveAction = async (recommendation: Recommendation, index: number) => {
        setSaving(index);
        try {
            const response = await fetch("http://127.0.0.1:8001/actions", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(recommendation),
            });
            if (!response.ok) throw new Error("Action could not be saved");
            setSaved((current) => ({ ...current, [index]: "Saved as Pending" }));
        } catch {
            setSaved((current) => ({ ...current, [index]: "Save failed" }));
        } finally {
            setSaving(null);
        }
    };

    return (
        <section className="civic-card">
            <div className="flex items-center justify-between border-b border-[var(--color-navy)]/10 pb-3">
                <div>
                    <h2 className="text-xl m-0 font-black uppercase tracking-tight">Recommended Actions</h2>
                    <p className="text-[10px] text-[#59616b] uppercase tracking-widest mt-1">
                        AI suggestions require official approval
                    </p>
                </div>
                <span className="text-[10px] font-black uppercase text-[var(--color-accent)]">Advisory</span>
            </div>
            <div className="mt-4 space-y-3">
                {recommendations.map((recommendation, index) => (
                    <div key={`${recommendation.risk_type}-${index}`} className="border border-[var(--color-navy)]/15 p-3 bg-white">
                        <div className="flex justify-between gap-3">
                            <span className="text-[10px] font-black uppercase text-[var(--color-navy)]">
                                {recommendation.risk_type} · {recommendation.priority}
                            </span>
                            <span className="text-[9px] font-bold text-[#59616b]">{recommendation.status}</span>
                        </div>
                        <p className="text-xs font-semibold text-[#333333] mt-2">{recommendation.reason}</p>
                        <p className="text-[9px] uppercase tracking-widest text-[#59616b] mt-2">
                            {recommendation.responsible_department} · {recommendation.location}
                        </p>
                        <button
                            type="button"
                            onClick={() => saveAction(recommendation, index)}
                            disabled={saving === index || Boolean(saved[index])}
                            className="mt-3 border border-[var(--color-navy)] px-3 py-1 text-[9px] font-black uppercase tracking-widest text-[var(--color-navy)] disabled:opacity-50"
                        >
                            {saved[index] || (saving === index ? "Saving..." : "Create Pending Action")}
                        </button>
                    </div>
                ))}
            </div>
        </section>
    );
}
