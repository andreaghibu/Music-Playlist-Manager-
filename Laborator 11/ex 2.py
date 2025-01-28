import numpy as np
import pandas as pd

# Set a random seed for reproducibility
np.random.seed(42)

# Parameters
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

# Generate dataset
data = []
for day in range(1, num_days + 1):
    num_products = np.random.randint(min_products, max_products + 1)  # Random number of products sold each day
    for _ in range(num_products):
        product_name = f"Produs_{np.random.randint(1, 21)}"  # Simulating 20 different products
        price = max(1, np.random.normal(average_price, std_dev_price))  # Normal distribution for prices
        quantity = np.random.randint(min_quantity, max_quantity + 1)  # Uniform distribution for quantities
        is_promotion = np.random.rand() < promotion_probability  # 30% chance of promotion

        if is_promotion:
            price *= (1 - promotion_discount)  # Apply 20% discount for promotions

        total_sales = price * quantity
        profit = total_sales * profit_margin  # Profit margin of 30%

        data.append([day, product_name, price, quantity, total_sales, profit])

# Create a DataFrame
columns = ["Zi", "Produs", "Pret", "Cantitate", "Total Vanzari", "Profit"]
df_sales = pd.DataFrame(data, columns=columns)

# 7. General statistics for dataset
mean_price = df_sales["Pret"].mean()
max_price = df_sales["Pret"].max()
min_price = df_sales["Pret"].min()

mean_quantity = df_sales["Cantitate"].mean()
max_quantity = df_sales["Cantitate"].max()
min_quantity = df_sales["Cantitate"].min()

mean_profit = df_sales["Profit"].mean()
max_profit = df_sales["Profit"].max()
min_profit = df_sales["Profit"].min()

# 8. Total sales and total profit for the 60-day period
total_sales = df_sales["Total Vanzari"].sum()
total_profit = df_sales["Profit"].sum()

# Print statistics
print("Statistici generale:")
print(f"Media prețurilor: {mean_price:.2f}, Maxim preț: {max_price:.2f}, Minim preț: {min_price:.2f}")
print(f"Media cantităților: {mean_quantity:.2f}, Maxim cantitate: {max_quantity}, Minim cantitate: {min_quantity}")
print(f"Media profitului: {mean_profit:.2f}, Maxim profit: {max_profit:.2f}, Minim profit: {min_profit:.2f}")
print(f"Total vânzări: {total_sales:.2f}, Profit total: {total_profit:.2f}")

# Display first few rows of the dataset
print("\nDataset generat (primele 10 rânduri):")
print(df_sales.head(10))
