"""
validation.py

Final validation of cleaned / warehouse-ready data.
Checks:
- Any remaining nulls in key fields?
- Any negative or zero UnitPrice / Quantity?
- Basic sanity metrics.
"""

from pathlib import Path
import pandas as pd


def validate_fact_sales(path: str | Path = "results/fact_sales_ready.csv") -> None:
    path = Path(path)
    df = pd.read_csv(path)

    print("=== VALIDATION: FACT_SALES_READY ===")
    print(f"Row count: {len(df)}")
    print("\nNull counts:")
    print(df.isnull().sum())

    # Check key columns (assumes these exist in your dataset)
    key_columns = ["InvoiceNo", "StockCode", "InvoiceDate", "CustomerID", "Country"]
    print("\nNulls in key columns:")
    for col in key_columns:
        if col in df.columns:
            print(f"{col}: {df[col].isnull().sum()}")

    # Check validity for Quantity and UnitPrice
    invalid_qty = df[df["Quantity"] <= 0]
    invalid_price = df[df["UnitPrice"] <= 0]

    print("\nInvalid Quantity (<= 0) rows:", len(invalid_qty))
    print("Invalid UnitPrice (<= 0) rows:", len(invalid_price))

    if len(invalid_qty) == 0 and len(invalid_price) == 0:
        print("\n FactSales data passed basic validity checks.")
    else:
        print("\n FactSales data still has invalid rows. Review needed.")


if __name__ == "__main__":
    validate_fact_sales()
