import pandas as pd

# ─────────────────────────────────────────────
# Ex01.py – Análise exploratória do CSV de classificação
# ─────────────────────────────────────────────

# Carregar dados
df = pd.read_csv("classification_results_trial_0001.csv")

print("=" * 60)
print("ANÁLISE EXPLORATÓRIA – classification_results_trial_0001.csv")
print("=" * 60)

# ── Inspeção inicial ──────────────────────────
print("\n--- head() ---")
print(df.head())

print("\n--- info() ---")
df.info()

print("\n--- describe() ---")
print(df.describe())

# ── 1. Contagem por real_class ────────────────
print("\n[1] Quantidade por real_class:")
print(df["real_class"].value_counts())

# ── 2. Imagens onde o modelo errou ───────────
df["acerto"] = df["real_class"] == df["predicted_class"]
erros = df[~df["acerto"]]
print(f"\n[2] Imagens com predição errada ({len(erros)} total):")
print(erros[["image_path", "real_class", "predicted_class",
             "prob_benign", "prob_malign"]].to_string(index=False))

# ── 3. Confiança nos erros ────────────────────
print("\n[3] Confiança do modelo nas predições erradas:")
erros_conf = erros.copy()
erros_conf["prob_predita"] = erros_conf.apply(
    lambda r: r["prob_malign"] if r["predicted_class"] == "malign"
              else r["prob_benign"], axis=1
)
print(erros_conf[["image_path", "real_class", "predicted_class",
                   "prob_predita"]].to_string(index=False))
confiantes = erros_conf[erros_conf["prob_predita"] >= 0.7]
print(f"\n  → {len(confiantes)} erros com confiança ≥ 70% (modelo errou mas estava 'confiante')")

# ── 4. TP, TN, FP, FN ────────────────────────
TP = len(df[(df["real_class"] == "malign") & (df["predicted_class"] == "malign")])
TN = len(df[(df["real_class"] == "benign") & (df["predicted_class"] == "benign")])
FP = len(df[(df["real_class"] == "benign") & (df["predicted_class"] == "malign")])
FN = len(df[(df["real_class"] == "malign") & (df["predicted_class"] == "benign")])

print(f"\n[4] Matriz de confusão:")
print(f"  TP (real malign, previsto malign) = {TP}")
print(f"  TN (real benign, previsto benign) = {TN}")
print(f"  FP (real benign, previsto malign) = {FP}")
print(f"  FN (real malign, previsto benign) = {FN}")

# ── 5. Métricas ───────────────────────────────
accuracy    = (TP + TN) / (TP + TN + FP + FN)
precision   = TP / (TP + FP) if (TP + FP) > 0 else 0
recall      = TP / (TP + FN) if (TP + FN) > 0 else 0
specificity = TN / (TN + FP) if (TN + FP) > 0 else 0

print(f"\n[5] Métricas:")
print(f"  Acurácia     = {accuracy:.4f}  ({accuracy*100:.2f}%)")
print(f"  Precisão     = {precision:.4f}  ({precision*100:.2f}%)")
print(f"  Recall       = {recall:.4f}  ({recall*100:.2f}%)")
print(f"  Especif.     = {specificity:.4f}  ({specificity*100:.2f}%)")

# ── 6. 5 benign com menor prob_benign ─────────
benign_df = df[df["real_class"] == "benign"].nsmallest(5, "prob_benign")
print("\n[6] 5 imagens benign com menor prob_benign:")
print(benign_df[["image_path", "prob_benign", "prob_malign",
                  "predicted_class"]].to_string(index=False))
print("  → Essas imagens têm características visuais atípicas para benign;")
print("    o modelo ficou inseguro (ou errou) — casos limítrofes importantes.")

# ── 7. 5 malign com maior prob_benign ─────────
malign_df = df[df["real_class"] == "malign"].nlargest(5, "prob_benign")
print("\n[7] 5 imagens malign com maior prob_benign:")
print(malign_df[["image_path", "prob_benign", "prob_malign",
                  "predicted_class"]].to_string(index=False))
print("  → O modelo subestimou a malignidade dessas imagens;")
print("    são casos de alto risco onde o modelo falhou — críticos em diagnóstico.")
