import pandas as pd
import matplotlib.pyplot as plt

# Lê o CSV usando vírgula como separador
df = pd.read_csv("C:\Users\ADM\Documents\lab materiais\fototransistor60.csv", sep=',')

# Converte tudo para string e depois para número
df["VCE [V]"] = pd.to_numeric(df["VCE [V]"].astype(str).str.replace(',', '.'), errors='coerce')
df["IC [mA]"] = pd.to_numeric(df["IC [mA]"].astype(str).str.replace(',', '.'), errors='coerce')

# Ordena pela tensão
df = df.sort_values(by="VCE [V]")

Vd = df["VCE [V]"]
Id = df["IC [mA]"]

plt.figure(figsize=(8,5))
plt.plot(Vd, Id, marker='o')
plt.title("Curva IC x VCE")
plt.xlabel("VCE (V)")
plt.ylabel("IC (mA)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.show()
