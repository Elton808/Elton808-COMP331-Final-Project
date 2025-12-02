# Elton808-COMP331-Final-Project
# Data Warehousing Quality Analysis – E-Commerce Retail Dataset

## 📌 Project Overview
This project analyzes data quality issues in a real-world **e-commerce transactions dataset**.  
The goal is to apply data warehousing concepts (Weeks 10–11), including:

- ETL quality assessment  
- Star schema readiness  
- Slowly Changing Dimensions (SCDs)  
- Referential integrity checks  
- Data quality dimensions (completeness, validity, consistency)

This repository contains:
- 🔍 Data profiling scripts  
- 🧹 Cleaning and validation transformations  
- 📊 Summary tables & visualizations  
- 📄 Final written analysis for the course report  

---

## 📂 Dataset Description
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

The dataset is stored as **data.csv** in this repository (if file size permits) or can be downloaded from the original source.

---

## 🎯 Objectives
### 1. Perform Data Quality Analysis
Using course concepts from Weeks 10–11:
- **Completeness** – identify null values, missing customers, missing descriptions  
- **Validity** – detect negative quantities, zero or negative prices, invalid dates  
- **Consistency** – duplicate records, inconsistent invoice patterns, cancelled invoices  
- **ETL readiness** – identify issues affecting Fact/Dimension tables  
- **Referential integrity** – detect missing keys for DimCustomer or DimProduct  

### 2. Create a Warehouse-Aligned Cleaning Strategy
- Handling returns (negative quantities)
- Rejecting invalid values
- Mapping missing customers to “Unknown Customer”
- Deduplicating rows
- Standardizing product descriptions

---

## 🏗️ Star Schema Context
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

## 📁 Repository Structure



