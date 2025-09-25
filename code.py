import json
import pandas as pd

# Baca file JSON
with open("rafareladzka_V3925056.json.json", "r") as f:
    data = json.load(f)

# Ubah setiap bagian JSON menjadi DataFrame
df_video = pd.DataFrame(data["data_video"])
df_pengguna = pd.DataFrame(data["data_pengguna"])
df_laporan = pd.DataFrame(data["data_laporan"])
df_analisis = pd.DataFrame(data["data_analisis"])

# Tampilkan tabel
print("=== Data Video ===")
print(df_video.head(), "\n")

print("=== Data Pengguna ===")
print(df_pengguna.head(), "\n")

print("=== Data Laporan ===")
print(df_laporan.head(), "\n")

print("=== Data Analisis ===")
print(df_analisis.head(), "\n")

# Jika ingin simpan ke Excel
with pd.ExcelWriter("rafarel_TIA_V3925056.xlsx") as writer:
    df_video.to_excel(writer, sheet_name="Data Video", index=False)
    df_pengguna.to_excel(writer, sheet_name="Data Pengguna", index=False)
    df_laporan.to_excel(writer, sheet_name="Data Laporan", index=False)
    df_analisis.to_excel(writer, sheet_name="Data Analisis", index=False)

print("Data berhasil disimpan ke rafarel_TIA_V3925056.xlsx")