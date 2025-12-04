import pandas as pd
from pathlib import Path

def run_profiling(data_path="data.csv", results_dir="results"):
    results_dir = Path(results_dir)
    results_dir.mkdir(exist_ok=True, parents=True)

    df = pd.read_csv(data_path, encoding="ISO-8859-1")

    # Missing values summary
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    summary = (
        pd.DataFrame({
            "column": df.columns,
            "missing_count": missing.values,
            "missing_percent": missing_pct.values,
        })
        .sort_values("missing_percent", ascending=False)
    )
    summary.to_csv(results_dir / "missing_values_summary.csv", index=False)

    # Duplicates
    dupes = df[df.duplicated()]
    dupes.to_csv(results_dir / "duplicates_report.csv", index=False)

    # Invalid quantity / price
    invalid_qty = df[df["Quantity"] <= 0]
    invalid_price = df[df["UnitPrice"] <= 0]

    invalid_qty.to_csv(results_dir / "invalid_quantity.csv", index=False)
    invalid_price.to_csv(results_dir / "invalid_price.csv", index=False)

    print("Profiling done. Files saved in 'results/'.")

if __name__ == "__main__":
    run_profiling()
