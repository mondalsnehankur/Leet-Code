# 💖 Longest Palindromic Substring

## 📌 Problem Statement

Given a string `s`, return the **longest palindromic substring** in `s`.

A **palindrome** is a string that reads the same forward and backward.

A **substring** is a contiguous sequence of characters within a string.

---

## 📝 Examples

### Example 1

**Input**

```text
s = "babad"
```

**Output**

```text
"bab"
```

**Explanation**

`"aba"` is also a valid answer since it is also the longest palindromic substring.

---

### Example 2

**Input**

```text
s = "cbbd"
```

**Output**

```text
"bb"
```

---

## 📋 Constraints

* `1 <= s.length <= 1000`
* `s` consists only of English letters and digits.

---

# 🎯 Objective

Find the **longest contiguous substring** that is a palindrome.

---

# 🚀 Approach 1: Brute Force

## 💡 Idea

Generate every possible substring and check whether it is a palindrome.

Keep track of the longest palindrome found.

---

## Algorithm

1. Generate all possible substrings.
2. Check whether each substring is a palindrome.
3. If it is longer than the current longest palindrome, update the answer.
4. Return the longest palindrome.

---

## Python Solution

```python
class Solution(object):
    def longestPalindrome(self, s):
        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]

                if substring == substring[::-1]:
                    if len(substring) > len(longest):
                        longest = substring

        return longest
```

---

## Complexity Analysis

| Metric           | Complexity |
| ---------------- | ---------- |
| Time Complexity  | **O(n³)**  |
| Space Complexity | **O(1)**   |

---

# 🚀 Approach 2: Expand Around Center (Recommended)

## 💡 Idea

Every palindrome has a center.

There are two possibilities:

* Odd-length palindrome

```text
racecar
   ↑
```

* Even-length palindrome

```text
abba
 ↑ ↑
```

Expand outward from every possible center while the characters match.

---

## Algorithm

1. Consider every index as the center of an odd-length palindrome.
2. Consider every pair of adjacent indices as the center of an even-length palindrome.
3. Expand outward while both characters are equal.
4. Update the longest palindrome whenever a larger one is found.

---

## Python Solution

```python
class Solution(object):
    def longestPalindrome(self, s):

        if len(s) < 2:
            return s

        start = 0
        maxLength = 1

        def expand(left, right):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(len(s)):

            left, right = expand(i, i)

            if right - left + 1 > maxLength:
                start = left
                maxLength = right - left + 1

            left, right = expand(i, i + 1)

            if right - left + 1 > maxLength:
                start = left
                maxLength = right - left + 1

        return s[start:start + maxLength]
```

---

## Complexity Analysis

| Metric           | Complexity |
| ---------------- | ---------- |
| Time Complexity  | **O(n²)**  |
| Space Complexity | **O(1)**   |

---

# 🚀 Approach 3: Dynamic Programming

## 💡 Idea

Use a 2D table `dp`.

`dp[i][j]` is `True` if the substring `s[i...j]` is a palindrome.

A substring is a palindrome if:

* First and last characters are equal.
* The substring inside them is also a palindrome.

---

## Algorithm

1. Mark every single character as a palindrome.
2. Check substrings of length 2.
3. Gradually increase the substring length.
4. Store results in the DP table.
5. Track the longest palindrome.

---

## Python Solution

```python
class Solution(object):

    def longestPalindrome(self, s):

        n = len(s)

        dp = [[False] * n for _ in range(n)]

        start = 0
        maxLength = 1

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1

                if s[i] == s[j]:

                    if length == 2 or dp[i + 1][j - 1]:

                        dp[i][j] = True

                        if length > maxLength:
                            start = i
                            maxLength = length

        return s[start:start + maxLength]
```

---

## Complexity Analysis

| Metric           | Complexity |
| ---------------- | ---------- |
| Time Complexity  | **O(n²)**  |
| Space Complexity | **O(n²)**  |

---

# 🚀 Approach 4: Manacher's Algorithm

## 💡 Idea

Manacher's Algorithm transforms the string so that odd-length and even-length palindromes are handled uniformly.

It reuses information from previously computed palindromes to avoid redundant comparisons, making it the fastest known algorithm for this problem.

---

## Algorithm

1. Transform the string by inserting separators (`#`) between characters.
2. Maintain:

   * Current palindrome center
   * Right boundary of the palindrome
3. Use symmetry to estimate palindrome lengths.
4. Expand only when necessary.
5. Return the longest palindrome.

---

## Python Solution

```python
class Solution(object):

    def longestPalindrome(self, s):

        if not s:
            return ""

        t = "^#" + "#".join(s) + "#$"

        p = [0] * len(t)

        center = 0
        right = 0

        for i in range(1, len(t) - 1):

            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1

            if i + p[i] > right:
                center = i
                right = i + p[i]

        maxLen = max(p)
        centerIndex = p.index(maxLen)

        start = (centerIndex - maxLen) // 2

        return s[start:start + maxLen]
```

---

## Complexity Analysis

| Metric           | Complexity |
| ---------------- | ---------- |
| Time Complexity  | **O(n)**   |
| Space Complexity | **O(n)**   |

---

# 🧠 Dry Run

### Input

```text
s = "babad"
```

Possible palindromes:

```text
b
a
bab
aba
b
a
d
```

Longest palindrome:

```text
bab
```

or

```text
aba
```

Both are accepted.

---

# 📊 Complexity Comparison

| Approach             | Time Complexity | Space Complexity | Difficulty |
| -------------------- | --------------- | ---------------- | ---------- |
| Brute Force          | **O(n³)**       | **O(1)**         | ⭐ Easy     |
| Expand Around Center | **O(n²)**       | **O(1)**         | ⭐⭐ Easy    |
| Dynamic Programming  | **O(n²)**       | **O(n²)**        | ⭐⭐⭐ Medium |
| Manacher's Algorithm | **O(n)**        | **O(n)**         | ⭐⭐⭐⭐⭐ Hard |

---

# 🏆 Best Approach

| Scenario                                      | Recommended Approach   |
| --------------------------------------------- | ---------------------- |
| Learning the problem                          | Brute Force            |
| Coding Interviews                             | ✅ Expand Around Center |
| Dynamic Programming practice                  | Dynamic Programming    |
| Competitive Programming / Advanced Algorithms | Manacher's Algorithm   |

---

# 🔑 Key Concepts

* Strings
* Palindrome
* Substring
* Brute Force
* Two Pointers
* Expand Around Center
* Dynamic Programming
* String Transformation
* Manacher's Algorithm

---

# 📖 Learning Outcomes

After solving this problem, you will understand:

* The difference between a **substring** and a **subsequence**.
* How to identify palindromes efficiently.
* Why expanding around the center avoids unnecessary work.
* How Dynamic Programming stores intermediate results.
* How Manacher's Algorithm achieves linear time by exploiting palindrome symmetry.
* The trade-offs between simplicity, speed, and memory usage.

---

# 🏷️ Tags

`String` `Palindrome` `Dynamic Programming` `Two Pointers` `Sliding Window Concept` `Manacher's Algorithm` `LeetCode` `Medium`

---

## 📚 Platform

* **Platform:** LeetCode
* **Problem Number:** 5
* **Difficulty:** Medium
