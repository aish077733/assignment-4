# assignment-4
 

## 📌 Overview

This repository contains implementations of **Constraint Satisfaction Problems (CSP)** using Python.
All problems are solved using the **Backtracking Algorithm**.

---

## 📂 Files Included

* `australia_map.py` → Map coloring for Australia
* `telangana_map.py` → Map coloring for Telangana districts
* `sudoku_csp.py` → Sudoku solver (9×9 grid)
* `cryptarithmetic.py` → Cryptarithmetic puzzle (SEND + MORE = MONEY)

---

## ⚙️ Requirements

* Python 3.x installed

To check:

```bash
python3 --version
```

---

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/aish07733/assignment-4.git
cd assignment-4
```

---

### Step 2: Run Each Program

#### 🔹 Australia Map Coloring

```bash
python3 australia_map.py
```

#### 🔹 Telangana Map Coloring

```bash
python3 telangana_map.py
```

#### 🔹 Sudoku Solver

```bash
python3 sudoku_csp.py
```

#### 🔹 Cryptarithmetic Problem

```bash
python3 cryptarithmetic.py
```

---

## 🧠 Concepts Used

* Constraint Satisfaction Problem (CSP)
* Backtracking Algorithm
* Variables, Domains, Constraints
* Constraint Checking

---

## 📝 Problem Explanation

### 1. Map Coloring

Each region is assigned a color such that **no two adjacent regions have the same color**.

---

### 2. Sudoku

Fill a 9×9 grid such that:

* Each row has numbers 1–9
* Each column has numbers 1–9
* Each 3×3 box has numbers 1–9

---

### 3. Cryptarithmetic

Assign digits to letters such that:

```
SEND + MORE = MONEY
```

Each letter represents a unique digit.

---

## 📊 Sample Output

### ✔ Map Coloring

```
{'WA': 'Red', 'NT': 'Green', 'SA': 'Blue', ...}
```

### ✔ Sudoku

```
[5, 3, 4, 6, 7, 8, 9, 1, 2]
...
```

### ✔ Cryptarithmetic

```
{'S': 9, 'E': 5, 'N': 6, 'D': 7, ...}
```

---

## 👩‍💻 Author

**Aishwarya Pamu**

---

 
