import pandas as pd

# Încarcă fișierul CSV
try:
    df = pd.read_csv("vanzari_companie.csv")  # Înlocuiește cu calea completă a fișierului tău
    print("Fișierul a fost încărcat cu succes!")
except Exception as e:
    print(f"Eroare la încărcarea fișierului: {e}")
    exit()

# Verifică primele rânduri și denumirile coloanelor
print("\nPrimele rânduri din dataset:")
print(df.head())
print("\nColoanele din dataset:")
print(df.columns)

# Normalizează denumirile coloanelor (eliminăm spațiile și le transformăm în litere mici)
df.columns = [col.strip().lower() for col in df.columns]
print("\nColoanele normalizate:")
print(df.columns)

# Verifică dacă există coloana cu date
if 'Data' in df.columns:
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce')
    print("\nColoana 'Data' a fost convertită în format datetime.")
else:
    print("Nu există o coloană cu date în fișier. Verificați denumirile coloanelor.")
    exit()

# -----------------------------
# Cele mai vândute produse pe lună
# -----------------------------
df['luna_an'] = df['Data'].dt.to_period('M')  # Extragem luna și anul
most_sold_products = (
    df.groupby(['luna_an', 'produs'])['cantitate vanduta']
    .sum()
    .reset_index()
    .sort_values(['luna_an', 'cantitate vanduta'], ascending=[True, False])
)
most_sold_per_month = most_sold_products.groupby('luna_an').first().reset_index()
print("\nCele mai vândute produse pe lună:")
print(most_sold_per_month)

# -----------------------------
# Venitul total pe fiecare produs
# -----------------------------
df['venit_total'] = df['cantitate vanduta'] * df['pret']
total_revenue_per_product = df.groupby('produs')['venit_total'].sum().reset_index()
print("\nVenitul total pe fiecare produs:")
print(total_revenue_per_product)

# -----------------------------
# Filtrarea vânzărilor pentru un interval de timp
# -----------------------------
start_date = '2024-01-01'
end_date = '2024-03-31'
filtered_sales = df[(df['Data'] >= start_date) & (df['Data'] <= end_date)]
print(f"\nVânzări între {start_date} și {end_date}:")
print(filtered_sales)

# -----------------------------
# Gruparea pe lună și an pentru venitul mediu lunar
# -----------------------------
monthly_average_revenue = df.groupby('luna_an')['venit_total'].mean().reset_index()
print("\nVenitul mediu lunar:")
print(monthly_average_revenue)

# -----------------------------
# Vizualizare rezultate (opțional)
# -----------------------------
try:
    import matplotlib.pyplot as plt

    # Evoluția venitului mediu lunar
    plt.figure(figsize=(10, 6))
    plt.bar(monthly_average_revenue['luna_an'].astype(str), monthly_average_revenue['venit_total'], color='skyblue')
    plt.title("Venitul mediu lunar", fontsize=14)
    plt.xlabel("Lună-An", fontsize=12)
    plt.ylabel("Venit Mediu (RON)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    # Cele mai vândute produse pe lună
    plt.figure(figsize=(10, 6))
    for luna, group in most_sold_products.groupby('luna_an'):
        plt.bar(group['produs'], group['cantitate vanduta'], label=str(luna))

    plt.title("Cele mai vândute produse pe lună", fontsize=14)
    plt.xlabel("Produse", fontsize=12)
    plt.ylabel("Cantitate vândută", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title="Luna")
    plt.tight_layout()
    plt.show()

except ImportError:
    print("Matplotlib nu este instalat. Puteți instala folosind: pip install matplotlib")
