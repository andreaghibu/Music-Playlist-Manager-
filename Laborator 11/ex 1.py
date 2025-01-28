import pandas as pd

try:
    df = pd.read_csv("vanzari_companie.csv", sep=',')
    print("Fișierul a fost încărcat cu succes!")
except Exception as e:
    print(f"Eroare la încărcarea fișierului: {e}")
    exit()


print("Coloanele din dataset:")
print(df.columns)

if 'Data' in df.columns:
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce')
else:
    print("Nu există o coloană cu date în fișier. Verificați denumirile coloanelor.")
    exit()

df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

df['luna_an'] = df['data'].dt.to_period('M')
most_sold_products = (
    df.groupby(['luna_an', 'produs'])['cantitate']
    .sum()
    .reset_index()
    .sort_values(['luna_an', 'cantitate'], ascending=[True, False])
)
most_sold_per_month = most_sold_products.groupby('luna_an').first().reset_index()
print("\nCele mai vândute produse pe lună:")
print(most_sold_per_month)

df['venit_total'] = df['cantitate'] * df['pret']
total_revenue_per_product = df.groupby('produs')['venit_total'].sum().reset_index()
print("\nVenitul total pe fiecare produs:")
print(total_revenue_per_product)


start_date = '2024-01-01'
end_date = '2024-03-31'
filtered_sales = df[(df['data'] >= start_date) & (df['data'] <= end_date)]
print(f"\nVânzări între {start_date} și {end_date}:")
print(filtered_sales)

monthly_average_revenue = df.groupby('luna_an')['venit_total'].mean().reset_index()
print("\nVenitul mediu lunar:")
print(monthly_average_revenue)

try:
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.bar(monthly_average_revenue['luna_an'].astype(str), monthly_average_revenue['venit_total'], color='skyblue')
    plt.title("Venitul mediu lunar", fontsize=14)
    plt.xlabel("Lună-An", fontsize=12)
    plt.ylabel("Venit Mediu (RON)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

except ImportError:
    print("Matplotlib nu este instalat. Puteți instala folosind: pip install matplotlib")
