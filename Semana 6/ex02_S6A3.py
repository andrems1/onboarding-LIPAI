import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("metrics.csv")
epochs = range(1, len(df) + 1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Curvas de Treino e Validação", fontsize=13, fontweight="bold")

BLUE   = "#1a56db"
ORANGE = "#f97316"

# ── Accuracy ────────────────────────────────────────────────────────
ax1.plot(epochs, df["train_acc"], color=BLUE,   linewidth=2, label="train")
ax1.plot(epochs, df["val_acc"],   color=ORANGE, linewidth=2, label="valid")
ax1.set_title("model accuracy", fontsize=11)
ax1.set_xlabel("epoch"); ax1.set_ylabel("accuracy")
ax1.legend(fontsize=9); ax1.grid(alpha=0.25)
ax1.spines[["top","right"]].set_visible(False)

# ── Loss ─────────────────────────────────────────────────────────────
ax2.plot(epochs, df["train_loss"], color=BLUE,   linewidth=2, label="train")
ax2.plot(epochs, df["val_loss"],   color=ORANGE, linewidth=2, label="valid")
ax2.set_title("model loss", fontsize=11)
ax2.set_xlabel("epoch"); ax2.set_ylabel("loss")
ax2.legend(fontsize=9); ax2.grid(alpha=0.25)
ax2.spines[["top","right"]].set_visible(False)

plt.tight_layout()
plt.savefig("ex02_graficos.png", dpi=150, bbox_inches="tight")
plt.close()
print("ex02_graficos.png salvo.")
