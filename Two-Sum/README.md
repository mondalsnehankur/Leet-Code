# 🧩 Two Sum

## 📌 Problem Statement

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`.

You may assume that:

- Each input has **exactly one solution**.
- You **may not use the same element twice**.
- The answer can be returned in **any order**.

---

## 📝 Examples

### Example 1

**Input**
```text
nums = [2,7,11,15]
target = 9
```

**Output**
```text
[0,1]
```

**Explanation**

```text
nums[0] + nums[1] = 2 + 7 = 9
```

---

### Example 2

**Input**
```text
nums = [3,2,4]
target = 6
```

**Output**
```text
[1,2]
```

---

### Example 3

**Input**
```text
nums = [3,3]
target = 6
```

**Output**
```text
[0,1]
```

---

## 📋 Constraints

- `2 <= nums.length <= 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`
- `-10⁹ <= target <= 10⁹`
- Exactly **one valid answer** exists.

---

## 💡 Approach 1: Brute Force

### Algorithm

1. Traverse every element in the array.
2. For each element, check every remaining element.
3. If the sum equals the target, return their indices.

### Time Complexity

```text
O(n²)
```

### Space Complexity

```text
O(1)
```

---

## 🚀 Approach 2: Hash Map (Optimal)

### Algorithm

1. Create an empty hash map.
2. Traverse the array once.
3. For each element:
   - Compute the complement:
     ```text
     complement = target - nums[i]
     ```
   - If the complement already exists in the hash map, return both indices.
   - Otherwise, store the current element and its index.

### Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(n)
```

---

## 📊 Complexity Comparison

| Approach | Time Complexity | Space Complexity |
|----------|-----------------|------------------|
| Brute Force | O(n²) | O(1) |
| Hash Map | O(n) | O(n) |

---

## 🎯 Key Concepts

- Arrays
- Hash Maps (Dictionary)
- One-pass traversal
- Time complexity optimization

---

## 📚 Learning Outcome

After solving this problem, you will understand:

- How to iterate through arrays efficiently.
- When a brute-force solution is acceptable.
- How hash maps reduce lookup time from **O(n)** to **O(1)**.
- The trade-off between **time** and **space** complexity.

---

## 🏷️ Tags

`Array` `Hash Map` `LeetCode` `Easy` `Interview Preparation`

---

> **Platform:** LeetCode  
> **Difficulty:** Easy
