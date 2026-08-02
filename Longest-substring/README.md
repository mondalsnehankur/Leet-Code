# 🔠 Longest Substring Without Repeating Characters

## 📌 Problem Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.

A **substring** is a contiguous sequence of characters within a string.

---

## 📝 Examples

### Example 1

**Input**

```text
s = "abcabcbb"
```

**Output**

```text
3
```

**Explanation**

The longest substring without repeating characters is `"abc"`, which has a length of **3**.

Other valid substrings of length 3 are `"bca"` and `"cab"`.

---

### Example 2

**Input**

```text
s = "bbbbb"
```

**Output**

```text
1
```

**Explanation**

The longest substring without repeating characters is `"b"`.

---

### Example 3

**Input**

```text
s = "pwwkew"
```

**Output**

```text
3
```

**Explanation**

The longest substring is `"wke"` with a length of **3**.

> **Note:** `"pwke"` is a subsequence, **not** a substring.

---

## 📋 Constraints

- `0 <= s.length <= 10⁵`
- `s` consists of:
  - English letters
  - Digits
  - Symbols
  - Spaces

---

# 💡 Approach 1: Brute Force

## Idea

Start from every character in the string and extend the substring until a duplicate character is found.

Keep track of the maximum substring length encountered.

---

## Algorithm

1. Iterate through every character as the starting point.
2. Create an empty set to store visited characters.
3. Extend the substring one character at a time.
4. If a duplicate character is encountered, stop expanding.
5. Update the maximum length.
6. Repeat for all starting positions.

---

## Python Solution

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):

        maxLength = 0

        for i in range(len(s)):

            seen = set()

            for j in range(i, len(s)):

                if s[j] in seen:
                    break

                seen.add(s[j])
                maxLength = max(maxLength, j - i + 1)

        return maxLength
```

---

## Complexity Analysis

| Metric | Complexity |
|---------|------------|
| Time Complexity | **O(n²)** |
| Space Complexity | **O(n)** |

---

# 🚀 Approach 2: Sliding Window (Optimal)

## Idea

Instead of restarting from every character, maintain a **sliding window** containing only unique characters.

- Expand the window by moving the right pointer.
- If a duplicate is found, shrink the window from the left until all characters are unique again.
- Track the maximum window size.

---

## Algorithm

1. Create an empty set.
2. Initialize two pointers:
   - `left`
   - `right`
3. Traverse the string using the `right` pointer.
4. If the current character already exists in the set:
   - Remove characters from the left until the duplicate is removed.
5. Add the current character to the set.
6. Update the maximum length.
7. Continue until the end of the string.

---

## Python Solution

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):

        charSet = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):

            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)

        return maxLength
```

---

# 🧠 Dry Run

### Input

```text
s = "abcabcbb"
```

| Left | Right | Current Window | Max Length |
|------|------:|----------------|-----------:|
| 0 | 0 | `a` | 1 |
| 0 | 1 | `ab` | 2 |
| 0 | 2 | `abc` | 3 |
| 1 | 3 | `bca` | 3 |
| 2 | 4 | `cab` | 3 |
| 3 | 5 | `abc` | 3 |
| 5 | 6 | `cb` | 3 |
| 7 | 7 | `b` | 3 |

**Final Answer**

```text
3
```

---

# 📊 Complexity Comparison

| Approach | Time Complexity | Space Complexity |
|----------|-----------------|------------------|
| Brute Force | O(n²) | O(n) |
| Sliding Window | **O(n)** | O(n) |

---

# 🔑 Key Concepts

- Strings
- Hash Set
- Sliding Window
- Two Pointers
- Brute Force Optimization

---

# 📖 Learning Outcomes

After solving this problem, you will understand:

- The difference between a **substring** and a **subsequence**.
- How to detect duplicate characters efficiently.
- How a **Hash Set** enables constant-time lookups.
- How the **Sliding Window** technique optimizes nested-loop solutions.
- The trade-off between brute-force and optimal approaches.

---

# 🏷️ Tags

`String` `Hash Set` `Sliding Window` `Two Pointers` `LeetCode` `Medium`

---

## 📚 Platform

- **Platform:** LeetCode
- **Problem Number:** 3
- **Difficulty:** Medium
