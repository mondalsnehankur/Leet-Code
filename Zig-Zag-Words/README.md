# Zigzag Conversion

A Python solution to the **Zigzag Conversion** problem from LeetCode. This implementation simulates writing characters in a zigzag pattern across multiple rows and then reads the rows sequentially to produce the converted string.

## 📌 Problem Statement

Given a string `s` and an integer `numRows`, write the string in a zigzag pattern across the specified number of rows and then return the string read row by row.

### Example 1

```text id="egmn19"
Input:
s = "PAYPALISHIRING"
numRows = 3

Output:
"PAHNAPLSIIGYIR"
```

Zigzag pattern:

```text id="4tl7th"
P   A   H   N
A P L S I I G
Y   I   R
```

---

### Example 2

```text id="9jz1s5"
Input:
s = "PAYPALISHIRING"
numRows = 4

Output:
"PINALSIGYAHRPI"
```

Zigzag pattern:

```text id="tpcjg0"
P     I     N
A   L S   I G
Y A   H R
P     I
```

---

## 💡 Approach

The solution simulates the zigzag traversal using an array of strings, where each element represents one row.

### Steps

1. Handle edge cases:

   * If `numRows == 1`
   * If `numRows >= len(s)`
   * Return the original string.

2. Create a list containing one empty string for each row.

3. Traverse every character in the input string.

4. Append each character to the current row.

5. Change direction whenever the first or last row is reached.

6. Join all rows together to obtain the final result.

---

## 🧠 Algorithm

```text id="i3qysu"
If numRows is 1 or greater than the string length:
    Return the original string

Create an array of empty strings for each row

Set currentRow = 0
Set goingDown = False

For each character:
    Append character to currentRow

    If currentRow is first or last row:
        Reverse direction

    Move up or down depending on direction

Return the concatenation of all rows
```

---

## ⏱ Time and Space Complexity

| Complexity | Value    |
| ---------- | -------- |
| Time       | **O(n)** |
| Space      | **O(n)** |

where **n** is the length of the input string.

---

## ▶️ Example Walkthrough

Input:

```text id="i1n1hd"
s = "PAYPALISHIRING"
numRows = 3
```

Rows after traversal:

```text id="jcrrwg"
Row 0: PAHN
Row 1: APLSIIIG
Row 2: YIR
```

Final Output:

```text id="cjlwmc"
PAHNAPLSIIGYIR
```

---

## 📂 Project Structure

```text id="k8c65r"
Zigzag-Conversion/
│
├── solution.py
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```bash id="q9ozfo"
git clone https://github.com/your-username/zigzag-conversion.git
```

2. Navigate to the project directory:

```bash id="hbm8ql"
cd zigzag-conversion
```

3. Run the solution:

```bash id="0mvwn3"
python solution.py
```

---

## 📚 Concepts Used

* Strings
* Arrays (Lists)
* Simulation
* Direction Tracking
* Conditional Statements
* Iteration
* String Concatenation

---

## 🎯 Suitable For

* LeetCode practice
* Data Structures and Algorithms preparation
* Coding interview preparation
* Python beginners learning string manipulation

---

## 🚀 Key Insight

Instead of explicitly constructing the zigzag matrix, the solution stores characters directly in their corresponding row. This eliminates unnecessary empty spaces and keeps the implementation efficient with **linear time complexity**.

---

## 📄 License

This project is open-source and intended for educational and learning purposes.
