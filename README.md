# 💳 Credit Card Discount Calculator

A simple **Python-based discount calculation program** that determines whether a customer is eligible for a **10% discount** based on their payment method, number of products purchased, and individual product prices.

The project demonstrates the use of **conditional statements, nested `if-else` logic, user input, arithmetic operations, and formatted output in Python**.

---

## 📌 Problem Statement

Write a Python program to provide a **10% discount** to a customer only when **all** of the following conditions are satisfied:

1. The customer pays using a **Credit Card**.
2. The customer purchases **at least 3 products**.
3. The price of **each product must be ₹500 or more**.
4. If all conditions are satisfied, calculate the total purchase amount and apply a **10% discount**.
5. If any condition is not satisfied, **no discount should be provided**.

---

## 🎯 Objective

The main objective of this program is to understand how multiple conditions can be combined using **nested conditional statements** in Python.

### Discount Eligibility

```text
Payment Method = Credit Card
        +
Number of Products >= 3
        +
Each Product Price >= ₹500
        ↓
   10% Discount
```

If any one of these conditions fails, the customer is **not eligible for the discount**.

---

## 🛠️ Technologies Used

* **Python 3**
* Conditional Statements (`if`, `elif`, `else`)
* Nested Conditional Statements
* User Input
* Arithmetic Operators
* F-Strings

---

## ⚙️ Program Logic

The program follows these steps:

### Step 1: Select Payment Method

The customer enters their payment method.

```python
mode = input("Enter the Payment Mode: ")
```

The program checks whether the payment method is **Credit Card**.

### Step 2: Enter Number of Products

If the payment method is a credit card, the customer enters the number of products purchased.

```python
product = int(input("Enter the Product Number: "))
```

The customer must purchase **at least 3 products**.

### Step 3: Enter Product Prices

The program accepts the prices of three products:

```python
P1 = float(input("Enter the price of Product 1: "))
P2 = float(input("Enter the price of Product 2: "))
P3 = float(input("Enter the price of Product 3: "))
```

Each product must satisfy the minimum price requirement.

### Step 4: Check Product Prices

```python
if P1 >= 500 and P2 >= 500 and P3 >= 500:
```

The `and` operator ensures that **all three products** satisfy the price condition.

### Step 5: Calculate Total

```python
total = P1 + P2 + P3
```

The prices of all three products are added together.

### Step 6: Apply 10% Discount

```python
discount = total * 0.10
final_amount = total - discount
```

The discount amount is calculated as 10% of the total purchase amount.

---

## 💻 Sample Execution

### ✅ Eligible Customer

```text
Enter the Payment Mode: Credit Card
Enter the Product Number: 3
Enter the price of Product 1: 600
Enter the price of Product 2: 800
Enter the price of Product 3: 1000

Total Amount: ₹2400
Discount: ₹240
Final Amount: ₹2160
```

The customer receives a **10% discount** because all eligibility conditions are satisfied.

---

### ❌ Payment Method Not Eligible

```text
Enter the Payment Mode: Cash

No discount available.
```

The customer is not eligible because the payment method is not a credit card.

---

### ❌ Less Than 3 Products

```text
Enter the Payment Mode: Credit Card
Enter the Product Number: 2

Discount not available. Minimum 3 products are required.
```

---

### ❌ Product Price Below ₹500

```text
Enter the Payment Mode: Credit Card
Enter the Product Number: 3
Enter the price of Product 1: 600
Enter the price of Product 2: 400
Enter the price of Product 3: 800

Discount not available. Each product must cost at least ₹500.
```

---

## 🔄 Program Flow

```text
              Start
                │
                ▼
       Enter Payment Mode
                │
                ▼
      Is it Credit Card?
          /          \
        No            Yes
        │              │
        ▼              ▼
   No Discount    Enter Product Count
                       │
                       ▼
              Products >= 3?
                  /       \
                No         Yes
                │            │
                ▼            ▼
           No Discount   Enter Prices
                             │
                             ▼
                  All Prices >= ₹500?
                       /        \
                     No          Yes
                     │             │
                     ▼             ▼
                No Discount    Calculate Total
                                    │
                                    ▼
                              Apply 10% Discount
                                    │
                                    ▼
                              Display Final Amount
```

---

## 🧮 Discount Formula

### Discount Amount

```text
Discount = Total Amount × 10 / 100
```

### Final Amount

```text
Final Amount = Total Amount − Discount
```

### Example

For three products:

```text
Product 1 = ₹600
Product 2 = ₹800
Product 3 = ₹1000
```

Total:

```text
₹600 + ₹800 + ₹1000 = ₹2400
```

10% discount:

```text
₹2400 × 10% = ₹240
```

Final amount:

```text
₹2400 − ₹240 = ₹2160
```

---

## 📚 Python Concepts Demonstrated

| Concept              | Usage                        |
| -------------------- | ---------------------------- |
| `input()`            | Accept user input            |
| `if-else`            | Decision making              |
| Nested conditions    | Check multiple requirements  |
| `and` operator       | Verify all conditions        |
| `float()`            | Accept decimal prices        |
| Arithmetic operators | Calculate total and discount |
| F-string             | Display formatted output     |

---

## ⚠️ Important Note About the Original Code

The original program uses:

```python
eval(input())
```

For example:

```python
mode = eval(input("Enter the Payment Mode "))
```

Using `eval()` for normal user input is **not recommended**, because it can execute arbitrary Python expressions.

A safer approach is:

```python
mode = input("Enter the Payment Mode: ")
product = int(input("Enter the Product Number: "))
P1 = float(input("Enter the price of Product 1: "))
```

Also, avoid unnecessary spaces in the payment-mode comparison. Instead of:

```python
if mode == "Credit Card ":
```

use:

```python
if mode.strip().lower() == "credit card":
```

This makes the program more reliable when users enter different capitalization or extra spaces.

---

## 🚀 Possible Improvements

This project can be extended by:

* Supporting any number of products instead of exactly three.
* Calculating the discount dynamically.
* Adding GST/tax calculation.
* Adding multiple payment methods.
* Providing different discount percentages for different purchase amounts.
* Adding input validation.
* Using functions to make the program modular.
* Creating a GUI using **Tkinter** or **CustomTkinter**.
* Storing purchase information in a database.

---

## 👨‍💻 Author

**Pranay Vishwanath Jadhao**

**Skills Demonstrated:** Python • Conditional Logic • Problem Solving • Basic Programming

---

## 📄 License

This project is created for **educational and learning purposes**.
