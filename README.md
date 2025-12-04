# Elton808-COMP331-Final-Project
# Building Trustworthy Data: ETL Quality and Data Cleaning for E-Commerce Transactions

This project analyzes data quality issues in a real world e-commerce transactions dataset.  
The goal is to apply data warehousing concepts, including:

- ETL quality assessment  
- Star schema readiness  
- Slowly Changing Dimensions (SCDs)  
- Referential integrity checks  
- Data quality dimensions (completeness, validity, consistency)

This repository contains:
- Data profiling scripts  
- Cleaning and validation transformations  
- Summary tables & visualizations  
- Final written analysis for the course report  

---

## Dataset Description
The dataset contains **541,909 rows** of invoice-level sales transactions, with fields:

| Column       | Description |
|--------------|-------------|
| InvoiceNo    | Unique invoice ID (C-prefixed = cancellations) |
| StockCode    | Product ID |
| Description  | Product description |
| Quantity     | Units sold (+) or returned (–) |
| InvoiceDate  | Timestamp of transaction |
| UnitPrice    | Price per unit |
| CustomerID   | Unique customer identifier (many missing) |
| Country      | Customer location |

The dataset is stored as data.csv in this repository.

---

## Objectives
1. Perform Data Quality Analysis
Using course concepts from Weeks 10–11:
- **Completeness** – identify null values, missing customers, missing descriptions  
- **Validity** – detect negative quantities, zero or negative prices, invalid dates  
- **Consistency** – duplicate records, inconsistent invoice patterns, cancelled invoices  
- **ETL readiness** – identify issues affecting Fact/Dimension tables  
- **Referential integrity** – detect missing keys for DimCustomer or DimProduct  

2. Create a Warehouse-Aligned Cleaning Strategy
- Handling returns (negative quantities)
- Rejecting invalid values
- Mapping missing customers to “Unknown Customer”
- Deduplicating rows
- Standardizing product descriptions

---

## Star Schema Context
This dataset is suitable for a retail star schema:

### **FactSales**
- InvoiceKey  
- DateKey  
- ProductKey  
- CustomerKey  
- CountryKey  
- Quantity  
- UnitPrice  
- ExtendedAmount  

### **Dimensions**
- **DimCustomer** – from CustomerID  
- **DimProduct** – from StockCode  
- **DimDate** – from InvoiceDate  
- **DimCountry** – from Country  

---

**Note: All steps below should be completed inside your project folder located on your Desktop.
Be sure to navigate to the project directory in Terminal before running any commands.**

Set Up Python Env & Run Scripts (macOS + BBEdit)

Step 1: Open Terminal.

Step 2: Navigate to the file dw-data-quality-project saved to your desktop
e.g('/Users/eltonbaretto/Documents/COMP 331/dw-data-quality-project')

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

===============

dw-data-quality-project/
├── README.md
├── requirements.txt
├── .gitignore
├── data.csv
├── scripts/
├── results/
├── notebooks/
└── report/

