#Building Trustworthy Data: ETL Quality and Data Cleaning for E-Commerce Transactions

##Project Overview
This project analyzes data quality issues in a real-world e-commerce transactions dataset as part of a Data Warehousing / Data Mining course (Weeks 10–11).

The focus is on:

- ETL quality and star schema readiness  
- Slowly Changing Dimensions (SCDs)  
- Referential integrity between fact and dimension tables  
- Data quality dimensions: completeness, validity, consistency

This repository contains:

- Data profiling scripts
- Cleaning and validation transformations
- Summary tables & visualizations
- Written analysis aligned with course requirements

---

##Dataset Description
The dataset contains invoice-level sales transactions from an online retailer.

**Key columns:**

| Column       | Description |
|--------------|-------------|
| `InvoiceNo`  | Unique invoice ID |
| `StockCode`  | Product ID |
| `Description`| Product description |
| `Quantity`   | Units sold (+) or returned (–) |
| `InvoiceDate`| Timestamp of transaction |
| `UnitPrice`  | Price per unit |
| `CustomerID` | Unique customer identifier (many missing) |
| `Country`    | Customer country |

Place the file as `data.csv` in the repo root (or update paths in scripts accordingly).

---

##Objectives

1. **Data Quality Analysis**
   - Check completeness (missing CustomerID, Description)
   - Check validity (negative quantities, zero/negative prices)
   - Check consistency (duplicates, cancelled invoices)
   - Evaluate ETL readiness and referential integrity for a star schema

2. **Cleaning Strategy for Warehousing**
   - Handle returns (negative quantities, cancelled invoices)
   - Map missing customers to an “Unknown Customer” member
   - Deduplicate records
   - Enforce simple business rules (no negative prices, no zero-quantity rows)

---

##StarSchema Context

A warehouse design for this dataset include:

### FactSales
- `InvoiceKey`
- `DateKey`
- `ProductKey`
- `CustomerKey`
- `CountryKey`
- `Quantity`
- `UnitPrice`
- `ExtendedAmount`

### DimCustomer
- `CustomerKey`
- `CustomerID`
- `Country`

### DimProduct
- `ProductKey`
- `StockCode`
- `Description`

### DimDate
- `DateKey`
- `FullDate`
- `Year`, `Month`, `Day`, `Quarter`, `DayOfWeek`

### DimCountry
- `CountryKey`
- `CountryName`

=============================================

**Note: All steps below should be completed inside your project folder located on your Desktop.
Be sure to navigate to the project directory in Terminal before running any commands.**

Set Up Python Env & Run Scripts (macOS + BBEdit)

Step 1: Open Terminal.

Step 2: Navigate to the file dw-data-quality-project saved to your desktop
e.g cd "/Users/eltonbaretto/Documents/COMP 331/dw-data-quality-project"

Step 3: Create a virtual environment: 
python3 -m venv venv

Step 4: Activate it: 
source venv/bin/activate

Step 5: Install requirements: 
pip install -r requirements.txt

Step 5.1: Run Profiling: 
python3 scripts/profiling.py

Step 5.2: Run Cleaning: 
python3 scripts/cleaning.py

Step 6: Create a Simple Jupyter Notebook for GitHub & screenshots: 
jupyter notebook



