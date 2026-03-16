import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

df = pd.read_csv("classification_results_trial_0001.csv")
df["acerto"] = df["real_class"] == df["predicted_class"]

# Calcular FP e FN para o gráfico 6
TP = len(df[(df["real_class"]=="malign") & (df["predicted_class"]=="malign")])
TN = len(df[(df["real_class"]=="benign") & (df["predicted_class"]=="benign")])
FP = len(df[(df["real_class"]=="benign") & (df["predicted_class"]=="malign")])
FN = len(df[(df["real_class"]=="malign") & (df["predicted_class"]=="benign")])

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle("Análise do Modelo de Classificação – classification_results_trial_0001.csv",
             fontsize=14, fontweight="bold", y=1.01)

BLUE   = "#1a56db"
ORANGE = "#f97316"
GREEN  = "#16a34a"
RED    = "#dc2626"
GRAY   = "#64748b"

# ── Gráfico 1: contagem por real_class ──────────────────────────────
ax = axes[0, 0]
counts_real = df["real_class"].value_counts()
bars = ax.bar(counts_real.index, counts_real.values,
              color=[RED, BLUE], edgecolor="white", linewidth=1.5, width=0.5)
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            str(int(bar.get_height())), ha="center", va="bottom", fontsize=11, fontweight="bold")
ax.set_title("Contagem por Classe Real", fontsize=11, fontweight="bold")
ax.set_xlabel("Classe"); ax.set_ylabel("Quantidade")
ax.set_ylim(0, max(counts_real.values) * 1.15)
ax.grid(axis="y", alpha=0.3); ax.spines[["top","right"]].set_visible(False)

# ── Gráfico 2: contagem por predicted_class ─────────────────────────
ax = axes[0, 1]
counts_pred = df["predicted_class"].value_counts()
bars = ax.bar(counts_pred.index, counts_pred.values,
              color=[RED, BLUE], edgecolor="white", linewidth=1.5, width=0.5)
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            str(int(bar.get_height())), ha="center", va="bottom", fontsize=11, fontweight="bold")
ax.set_title("Contagem por Classe Predita", fontsize=11, fontweight="bold")
ax.set_xlabel("Classe"); ax.set_ylabel("Quantidade")
ax.set_ylim(0, max(counts_pred.values) * 1.15)
ax.grid(axis="y", alpha=0.3); ax.spines[["top","right"]].set_visible(False)

# ── Gráfico 3: histograma prob_benign ───────────────────────────────
ax = axes[0, 2]
ax.hist(df["prob_benign"], bins=20, color=BLUE, edgecolor="white", alpha=0.85)
ax.axvline(df["prob_benign"].mean(), color=RED, linestyle="--", linewidth=1.5,
           label=f"Média: {df['prob_benign'].mean():.3f}")
ax.set_title("Histograma – prob_benign", fontsize=11, fontweight="bold")
ax.set_xlabel("Probabilidade Benigno"); ax.set_ylabel("Frequência")
ax.legend(fontsize=9); ax.grid(axis="y", alpha=0.3)
ax.spines[["top","right"]].set_visible(False)

# ── Gráfico 4: histograma prob_malign ───────────────────────────────
ax = axes[1, 0]
ax.hist(df["prob_malign"], bins=20, color=RED, edgecolor="white", alpha=0.85)
ax.axvline(df["prob_malign"].mean(), color=BLUE, linestyle="--", linewidth=1.5,
           label=f"Média: {df['prob_malign'].mean():.3f}")
ax.set_title("Histograma – prob_malign", fontsize=11, fontweight="bold")
ax.set_xlabel("Probabilidade Maligno"); ax.set_ylabel("Frequência")
ax.legend(fontsize=9); ax.grid(axis="y", alpha=0.3)
ax.spines[["top","right"]].set_visible(False)

# ── Gráfico 5: scatter acerto vs erro ───────────────────────────────
ax = axes[1, 1]
acertos = df[df["acerto"]]
erros   = df[~df["acerto"]]
ax.scatter(acertos["prob_benign"], acertos["prob_malign"],
           c=GREEN, alpha=0.65, s=50, label=f"Acerto ({len(acertos)})", edgecolors="white", linewidths=0.5)
ax.scatter(erros["prob_benign"], erros["prob_malign"],
           c=RED, alpha=0.9, s=80, marker="X", label=f"Erro ({len(erros)})", edgecolors="white", linewidths=0.5)
ax.plot([0,1],[1,0], color=GRAY, linestyle="--", linewidth=1, alpha=0.5)
ax.set_title("Scatter – Acerto vs Erro", fontsize=11, fontweight="bold")
ax.set_xlabel("prob_benign"); ax.set_ylabel("prob_malign")
ax.legend(fontsize=9); ax.grid(alpha=0.2)
ax.spines[["top","right"]].set_visible(False)

# ── Gráfico 6: FP vs FN ─────────────────────────────────────────────
ax = axes[1, 2]
labels = [f"FP\n(benign→malign)\n{FP}", f"FN\n(malign→benign)\n{FN}"]
vals   = [FP, FN]
colors_bar = [ORANGE, RED]
bars = ax.bar(labels, vals, color=colors_bar, edgecolor="white", linewidth=1.5, width=0.4)
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
            str(int(bar.get_height())), ha="center", va="bottom", fontsize=13, fontweight="bold")
ax.set_title("Erros por Tipo: FP vs FN", fontsize=11, fontweight="bold")
ax.set_ylabel("Quantidade"); ax.set_ylim(0, max(vals) * 1.3)
ax.grid(axis="y", alpha=0.3); ax.spines[["top","right"]].set_visible(False)
ax.text(0.5, -0.22,
        "FN é mais preocupante em contexto médico:\ncasos malignos não detectados podem atrasar tratamento.",
        ha="center", transform=ax.transAxes, fontsize=8, color=RED, style="italic")

plt.tight_layout()
plt.savefig("ex01_graficos.png", dpi=150, bbox_inches="tight")
plt.close()
print("ex01_graficos.png salvo.")
