# 🧠 Python `defaultdict` Quick Reference

## 📦 `collections.defaultdict` Overview

A `defaultdict` is like a regular `dict`, but with a default value generator for missing keys. It automatically initializes keys so you don’t need to check or set defaults manually.

### 📥 Import

```python
from collections import defaultdict
```

---

## ⚙️ Common Initialization Types

| Type                | Default Factory            | Description          | Example Use Case                |
| ------------------- | -------------------------- | -------------------- | ------------------------------- |
| `int`               | `defaultdict(int)`         | Default is `0`       | Frequency counters, prefix sums |
| `list`              | `defaultdict(list)`        | Default is `[]`      | Grouping items, adjacency lists |
| `set`               | `defaultdict(set)`         | Default is `set()`   | Uniquely grouped values         |
| `lambda: <default>` | `defaultdict(lambda: 999)` | Custom default value | Edge-case initialization        |

---

## 🔁 Methods and Behavior

| Feature                      | Description                                             | Time Complexity | Sample Output Example                         |
| ---------------------------- | ------------------------------------------------------- | --------------- | --------------------------------------------- |
| Auto-initialization          | Key initializes automatically with factory default      | O(1)            | `d['a'] += 1` → `{'a': 1}`                    |
| Supports standard `dict` ops | `get()`, `items()`, `pop()`, etc.                       | Same as `dict`  | Works identically, but safer for missing keys |
| Factory remains callable     | Can introspect default factory using `.default_factory` | O(1)            | `d.default_factory` returns `<class 'int'>`   |

---

## 🧪 Sample Code Snippets and Output

### 🧮 Frequency Counter (`int`)

```python
from collections import defaultdict

freq = defaultdict(int)
for ch in "mississippi":
    freq[ch] += 1

print(freq)
```

**Output:**

```python
defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})
```

---

### 🔗 Adjacency List (`list`)

```python
edges = [(0, 1), (0, 2), (1, 3)]

graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)

print(graph)
```

**Output:**

```python
defaultdict(<class 'list'>, {0: [1, 2], 1: [3]})
```

---

### 🧺 Grouping by Category (`list`)

```python
data = [('fruit', 'apple'), ('fruit', 'banana'), ('veg', 'carrot')]

grouped = defaultdict(list)
for category, item in data:
    grouped[category].append(item)

print(grouped)
```

**Output:**

```python
defaultdict(<class 'list'>, {'fruit': ['apple', 'banana'], 'veg': ['carrot']})
```

---

## 🧩 Common LeetCode Problem Patterns

### 🔁 Frequency Map without Key Checks

```python
count = defaultdict(int)
for num in nums:
    count[num] += 1  # no need to check if key exists!
```

### 🌊 Sliding Window with `int` map

* Track counts in real-time with cleaner syntax:

```python
window = defaultdict(int)
left = 0
for right in range(len(s)):
    window[s[right]] += 1
    # shrink window as needed
```

### 🧵 Grouping Anagrams

```python
anagrams = defaultdict(list)
for word in words:
    key = tuple(sorted(word))
    anagrams[key].append(word)
```

### 🌐 Graph Traversals

```python
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
# No need to check if u in graph before appending
```

---

## 💡 Tips

* Use `defaultdict` to **avoid `KeyError`** and eliminate boilerplate `if key not in dict` code.
* Great for **dynamic data structures** like frequency maps, graphs, or grouped lists.
* Keep in mind: `defaultdict` still raises `KeyError` if accessed with a missing key and no default factory set.

---
