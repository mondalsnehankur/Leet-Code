# Median of Two Sorted Arrays

A Python solution to the **Median of Two Sorted Arrays** problem from LeetCode. The solution merges two sorted arrays, sorts the combined array, and computes the median based on whether the total number of elements is odd or even.

## 📌 Problem Statement

Given two sorted integer arrays `nums1` and `nums2` of sizes `m` and `n`, return the median of the two sorted arrays.

**Examples**

```text
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0
```

```text
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.5
```

---

## 💡 Approach

The solution follows these steps:

1. Merge both input arrays.
2. Sort the merged array.
3. Find the total number of elements.
4. If the length is odd, return the middle element.
5. If the length is even, return the average of the two middle elements.

---

## 🧠 Algorithm

```text
1. Combine nums1 and nums2.
2. Sort the combined array.
3. Calculate the total number of elements.
4. If length is odd:
      Return the middle element.
5. Otherwise:
      Return the average of the two middle elements.
```

---

## ⏱ Time and Space Complexity

| Complexity | Value                     |
| ---------- | ------------------------- |
| Time       | **O((m + n) log(m + n))** |
| Space      | **O(m + n)**              |

> **Note:** Although this solution is simple and easy to understand, the original LeetCode problem requires an **O(log(m + n))** algorithm. This implementation does **not** satisfy that optimal time complexity because it performs a full sort.

---

## ▶️ Example Walkthrough

### Example 1

```text
nums1 = [1, 3]
nums2 = [2]
```

Merged array:

```text
[1, 2, 3]
```

Median:

```text
2.0
```

---

### Example 2

```text
nums1 = [1, 2]
nums2 = [3, 4]
```

Merged array:

```text
[1, 2, 3, 4]
```

Median:

```text
(2 + 3) / 2 = 2.5
```

---

## 📂 Project Structure

```text
Median-of-Two-Sorted-Arrays/
│
├── solution.py
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/median-of-two-sorted-arrays.git
```

2. Navigate to the project folder:

```bash
cd median-of-two-sorted-arrays
```

3. Run the Python solution:

```bash
python solution.py
```

---

## 📚 Concepts Used

* Arrays (Lists)
* Sorting
* Merging Lists
* Conditional Statements
* Integer Division
* Median Calculation
* Time Complexity Analysis

---

## 🎯 Suitable For

* LeetCode beginners
* Data Structures & Algorithms practice
* Coding interview preparation
* Python programming practice

---

## 🚀 Possible Optimization

The optimal solution uses **binary search** on the smaller array to partition both arrays correctly, achieving **O(log(min(m, n)))** time complexity while using **O(1)** extra space.

---

## 📄 License

This project is open-source and intended for educational and learning purposes.
