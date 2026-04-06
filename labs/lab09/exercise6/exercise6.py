import pandas as pd

def critical_inventory(filename):
    df = pd.read_csv(filename)
    total_products = len(df)

    critical_filter = (df['StockLevel'] < df['ReorderThreshold']) & (df['DaysSinceRestock'] > 30)
    df_critical = df[critical_filter]
    
    critical_count = len(df_critical)
    critical_products = set(df_critical['ProductName'])

    return {
        "total_products": total_products,
        "critical_count": critical_count,
        "critical_products": critical_products
    }

result = critical_inventory("labs/lab09/data/inventory.csv")
print(f"total_products: {result["total_products"]}")
print(f"critical_count: {result["critical_count"]}")
print(f"critical_products: {result["critical_products"]}")

# {
#     "total_products": 50,
#     "critical_count": 7,
#     "critical_products": {"Laptop_X1", "Monitor_Pro", "Keyboard_Mech", ...}
# }