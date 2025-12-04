import pandas as pd
from pathlib import Path

def run_cleaning(data_path="data.csv", results_dir="results"):
    results_dir = Path(results_dir)
    results_dir.mkdir(exist_ok=True, parents=True)

    df = pd.read_csv(data_path, encoding="ISO-8859-1")

    # Remove exact duplicates
    df = df.drop_duplicates()

    # Split sales (Quantity > 0) and returns (Quantity < 0)
    sales = df[df["Quantity"] > 0].copy()
    returns = df[df["Quantity"] < 0].copy()

    sales["TransactionType"] = "SALE"
    returns["TransactionType"] = "RETURN"

    # Missing CustomerID -> Unknown (-1)
    sales["CustomerID"] = sales["CustomerID"].fillna(-1)

    # Enforce business rule: keep only UnitPrice > 0
    sales = sales[sales["UnitPrice"] > 0]

    # Add ExtendedAmount
    sales["ExtendedAmount"] = sales["Quantity"] * sales["UnitPrice"]

    sales.to_csv(results_dir / "cleaned_sales.csv", index=False)
    returns.to_csv(results_dir / "cleaned_returns.csv", index=False)
    sales.to_csv(results_dir / "fact_sales_ready.csv", index=False)

    print("Cleaning done. Cleaned files saved in 'results/'.")

if __name__ == "__main__":
    run_cleaning()
