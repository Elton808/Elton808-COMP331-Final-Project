"""
etl_pipeline.py

Simple orchestration script:
1. Run profiling on raw data
2. Run cleaning to produce fact_sales_ready.csv
3. Run validation on cleaned data
"""

from scripts import profiling, cleaning, validation


def main():
    # 1. Profiling
    print("\n=== STEP 1: PROFILING ===")
    profiling.run_profiling("data.csv")

    # 2. Cleaning
    print("\n=== STEP 2: CLEANING ===")
    _, _, fact_sales_path = cleaning.run_cleaning("data.csv", "results")

    # 3. Validation
    print("\n=== STEP 3: VALIDATION ===")
    validation.validate_fact_sales(fact_sales_path)

    print("\nPipeline complete.")


if __name__ == "__main__":
    main()
	