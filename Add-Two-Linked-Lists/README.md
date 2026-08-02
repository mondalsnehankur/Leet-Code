# ➕ Add Two Numbers

## 📌 Problem Statement

You are given two **non-empty linked lists** representing two non-negative integers.

The digits are stored in **reverse order**, and each node contains a single digit.

Add the two numbers and return the sum as a **linked list**.

You may assume that the two numbers do **not contain leading zeros**, except the number `0` itself.

---

## 📝 Examples

### Example 1

**Input**

```text
l1 = [2,4,3]
l2 = [5,6,4]
```

**Output**

```text
[7,0,8]
```

**Explanation**

```text
342 + 465 = 807
```

Since the digits are stored in reverse order:

```text
2 → 4 → 3 represents 342
5 → 6 → 4 represents 465
```

The result is

```text
7 → 0 → 8
```

---

### Example 2

**Input**

```text
l1 = [0]
l2 = [0]
```

**Output**

```text
[0]
```

---

### Example 3

**Input**

```text
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
```

**Output**

```text
[8,9,9,9,0,0,0,1]
```

---

## 📋 Constraints

- `1 <= Number of Nodes <= 100`
- `0 <= Node.val <= 9`
- The linked lists represent numbers with **no leading zeros** (except the number `0`).

---

# 💡 Approach

## Idea

Traverse both linked lists simultaneously.

For each pair of nodes:

1. Read the current digit from each list.
2. Add both digits along with any carry from the previous step.
3. Store the one's digit in a new node.
4. Carry the ten's digit to the next iteration.
5. Continue until both linked lists are exhausted and there is no carry remaining.

A **dummy node** is used to simplify construction of the answer linked list.

---

## Algorithm

1. Create a dummy node.
2. Initialize a pointer (`current`) to the dummy node.
3. Initialize `carry = 0`.
4. Traverse both linked lists while either list has nodes or carry is non-zero.
5. Read values from the current nodes (use `0` if a list has ended).
6. Compute:
   ```
   total = val1 + val2 + carry
   ```
7. Update:
   ```
   carry = total // 10
   digit = total % 10
   ```
8. Create a new node containing `digit`.
9. Move all pointers forward.
10. Return `dummy.next`.

---

# 🧠 Dry Run

### Input

```text
l1 = 2 → 4 → 3
l2 = 5 → 6 → 4
```

### Iteration 1

```text
2 + 5 = 7
```

Carry:

```text
0
```

Result:

```text
7
```

---

### Iteration 2

```text
4 + 6 + 0 = 10
```

Store

```text
0
```

Carry

```text
1
```

Result

```text
7 → 0
```

---

### Iteration 3

```text
3 + 4 + 1 = 8
```

Carry

```text
0
```

Final Result

```text
7 → 0 → 8
```

---

# 💻 Python Solution

```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
```

---

# 📊 Complexity Analysis

| Metric | Complexity |
|---------|------------|
| Time Complexity | **O(max(m, n))** |
| Space Complexity | **O(max(m, n))** |

where

- `m` = length of first linked list
- `n` = length of second linked list

---

# 🔑 Key Concepts

- Linked List
- Dummy Node
- Carry Forward
- Pointer Manipulation
- Simulation

---

# 📖 Learning Outcomes

After solving this problem, you will understand:

- How to traverse two linked lists simultaneously.
- How to build a new linked list.
- Why a dummy node simplifies linked list construction.
- How to manage carry while adding numbers digit by digit.
- How to solve linked list problems using pointer manipulation.

---

# 🏷️ Tags

`Linked List` `Math` `Simulation` `LeetCode` `Medium`

---

## 📚 Platform

**LeetCode**

**Difficulty:** Medium
