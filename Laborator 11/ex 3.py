import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Generare dataset (folosind codul anterior, fără a-l afișa din nou)
np.random.seed(42)

num_days = 60
min_products = 5
max_products = 15
average_price = 40
std_dev_price = 8
min_quantity = 1
max_quantity = 10
promotion_probability = 0.3
promotion_discount = 0.2
profit_margin = 0.3

data = []
for day in range(1, num_days + 1):
    num_products = np.random.randint(min_products, max_products + 1)
    for _ in range(num_products):
        product_name = f"Produs_{np.random.randint(1, 21)}"
        price = max(1, np.random.normal(average_price, std_dev_price))
        quantity = np.random.randint(min_quantity, max_quantity + 1)
        is_promotion = np.random.rand() < promotion_probability
        original_price = price
        if is_promotion:
            price *= (1 - promotion_discount)
        total_sales = price * quantity
        profit = total_sales * profit_margin
        data.append([day, product_name, original_price, price, quantity, total_sales, profit, is_promotion])

columns = ["Zi", "Produs", "Pret Original", "Pret Final", "Cantitate", "Total Vanzari", "Profit", "Promotie"]
df_sales = pd.DataFrame(data, columns=columns)

# -----------------------------
# Evolutia veniturilor si profitului pe zile
# -----------------------------
daily_totals = df_sales.groupby("Zi")[["Total Vanzari", "Profit"]].sum().reset_index()

plt.figure(figsize=(14, 6))
plt.plot(daily_totals["Zi"], daily_totals["Total Vanzari"], label="Total Vânzări", marker="o")
plt.plot(daily_totals["Zi"], daily_totals["Profit"], label="Profit", marker="o", linestyle="--")
plt.title("Evoluția veniturilor și profitului pe zile", fontsize=16)
plt.xlabel("Zi", fontsize=12)
plt.ylabel("Valoare (RON)", fontsize=12)
plt.legend()
plt.grid()
plt.show()

# -----------------------------
# Distributia preturilor si cantitatilor vandute
# -----------------------------
plt.figure(figsize=(14, 6))

# Distribuția prețurilor
plt.subplot(1, 2, 1)
sns.histplot(df_sales["Pret Final"], bins=20, kde=True, color="blue")
plt.title("Distribuția prețurilor finale", fontsize=14)
plt.xlabel("Preț Final (RON)", fontsize=12)
plt.ylabel("Frecvență", fontsize=12)

# Distribuția cantităților
plt.subplot(1, 2, 2)
sns.histplot(df_sales["Cantitate"], bins=10, kde=True, color="green")
plt.title("Distribuția cantităților vândute", fontsize=14)
plt.xlabel("Cantitate", fontsize=12)
plt.ylabel("Frecvență", fontsize=12)

plt.tight_layout()
plt.show()

# -----------------------------
# Vizualizarea promotiilor
# -----------------------------
promotions = df_sales[df_sales["Promotie"]]
no_promotions = df_sales[~df_sales["Promotie"]]

# Calcul impact promovare
avg_price_promotion = promotions["Pret Final"].mean()
avg_price_no_promotion = no_promotions["Pret Final"].mean()

plt.figure(figsize=(10, 6))
sns.barplot(x=["Fără Promoție", "Cu Promoție"], y=[avg_price_no_promotion, avg_price_promotion], palette="viridis")
plt.title("Impactul promoțiilor asupra prețurilor", fontsize=16)
plt.ylabel("Preț Mediu Final (RON)", fontsize=12)
plt.xlabel("Stare Promoție", fontsize=12)
plt.show()
