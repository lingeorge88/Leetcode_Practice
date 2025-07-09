Absolutely! Here's the expanded `.md` file with **time complexities** added for each method, plus a deeper dive into common **LeetCode problem patterns** and how `dict` and `Counter` shine in those situations 🚀

# 🧠 Python Dictionary & Counter Quick Reference

## 📘 Regular `dict` Methods

| Method                     | Description                                                   | Time Complexity | LeetCode Use Cases                                      |
|----------------------------|---------------------------------------------------------------|------------------|----------------------------------------------------------|
| `get(key, default)`        | Safely retrieve value, return `default` if not found          | O(1)             | Frequency counts, edge-safe lookups                     |
| `pop(key, default)`        | Remove and return a key's value or return `default` if absent | O(1)             | Cache invalidation, map cleanup                         |
| `items()` / `keys()` / `values()` | Iterable views for entries/keys/values                          | O(n)             | Iterating key-value pairs or scanning sets              |
| `update(dict2)`            | Merge another dictionary's entries                            | O(len(dict2))    | Merging DP states, cumulative mappings                  |
| `setdefault(key, default)` | Insert key with `default` if not already present              | O(1)             | Grouping items, initializing frequency/categorization   |
| `copy()`                   | Shallow copy of a dictionary                                  | O(n)             | Save states before mutation (e.g., backtracking)        |

---

## 💪 `collections.Counter` Methods

| Method                     | Description                                                   | Time Complexity | LeetCode Use Cases                                      |
|----------------------------|---------------------------------------------------------------|------------------|----------------------------------------------------------|
| `Counter(iterable)`        | Build counter from iterable (like list or string)             | O(n)             | Quick frequency tables (e.g. anagram, majority element) |
| `update(iterable)`         | Add counts from iterable                                      | O(k)             | Streaming count updates (e.g. inventory, polling)        |
| `subtract(iterable)`       | Subtract counts, allowing negatives                           | O(k)             | Compare resource usage, differences in arrays           |
| `most_common(n)`           | Get `n` most frequent elements                                | O(n log n)       | Top-K frequent elements problems                        |
| `elements()`               | Expand back to list-like format                               | O(n)             | Restore inputs, permutations from frequency             |
| `+`, `-`, `&`, `|`         | Combine or intersect Counters                                 | O(n)             | Inventory merging, comparing datasets                   |

📝 *`n` is the number of unique keys, `k` is the number of elements added/subtracted.*

---

## 🧩 Common LeetCode Problem Patterns

### 📊 Frequency Map / Histogram Patterns
Use `dict` or `Counter` to efficiently count occurrences:

- 🔁 **Anagram detection**: Compare `Counter`s or use sorted tuples
- 💬 **Longest substring with k distinct characters**: Track char frequencies in window
- 🧮 **Majority element / Element that appears > n/2 times**: Count then filter

### 🧼 Greedy & Inventory Management
Use `Counter` and `dict` to track item availability and make real-time decisions:

- 🛒 **Task Scheduler**: Use `Counter.most_common()` and heap to balance cooldowns
- ⛏ **Resource allocation**: Track availability or usage with `subtract()`

### 🔐 Hash Map Patterns
Use `dict` for **constant-time lookups** or key-based grouping:

- 💲 **Two Sum / k Sum**: Store complements in map for O(1) search
- 🔁 **Subarray sum equals k**: Store cumulative prefix sums
- 🧵 **Group Anagrams**: Use sorted tuple or `Counter` as a key

### 🔄 Sliding Window
Track dynamic content using frequency maps:

- 👁️ **Minimum window substring**
- 🧼 **Longest substring without repeating characters**

### 🌐 Graph / Trie / Union-Find
Use `dict` for dynamic adjacency lists or parent lookup:

- 🔗 **Alien Dictionary**: Map graph relationships between characters
- 🏝️ **Number of islands** (DFS with coordinate dicts)

---

💡 **Tip**: Anytime you're counting, grouping, caching, or tracking things uniquely, `dict` and `Counter` are your go-to data structures. They’re the Swiss Army knives of coding interviews.

