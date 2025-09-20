# Inventory Management Project 

# 🏠 Inventory Management System (Python)

A simple **command-line based Inventory & Sales Management System** built with Python.  
This program helps store owners or hostel managers keep track of **products, sales, and stock updates** in real-time.  

---

## 🚀 Features

- **📦 Inventory Display**
  - Reads product data from `Inventory.txt`
  - Displays products in a clean tabular format (ID, Name, Price, Quantity)

- **👤 Customer Purchase**
  - Takes user details (Name, Mobile, Email)
  - Lets customer choose Product ID & Quantity

- **💰 Automatic Billing**
  - Calculates total bill (`Price × Quantity`)
  - Shows product details and billing summary
  - Handles low-stock situations with a choice to buy available quantity

- **📝 Sales Recording**
  - Appends every sale into `Sale.txt` with:
    - Customer info
    - Product ID
    - Quantity bought
    - Total bill
    - Date & Time of purchase

- **📉 Stock Updates**
  - Deducts sold quantity from `Inventory.txt`
  - Prevents overselling
  - Sets stock to **0** if product is fully sold

---


---

## ▶️ Usage

### 1️⃣ Clone Repo
```bash
git clone https://github.com/<your-username>/InventoryManagement.git
cd InventoryManagement

### 2️⃣ Run Script
```python main.py


### 3️⃣ Enter Details

``` Name, Mobile Number, Email
``` Product ID and Quantity



ID    Product Name             Price (₹)   Quantity  
-------------------------------------------------------
101   Notebook                 50          20        
102   Pen                      10          100       

 Enter Username: John
 Enter Mobile Number: 9876543210
 Enter Mail: john@example.com
 Enter Product ID: 101
 Enter Product Quantity: 2

----------------------------
Product Name     : Notebook
Product Price    : 50
Product Quantity : 20
----------------------------
Bill Amount      : 100
----------------------------




## 📂 File Structure

