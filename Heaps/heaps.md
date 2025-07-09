# Python heapq Operations & Runtime Guide

## Overview
Python's `heapq` module implements a **min-heap** (binary heap) data structure using regular Python lists. It provides heap operations with efficient time complexities.

## Import Syntax

### Option 1: Import the module (Recommended)
```python
import heapq
heapq.heappush(heap, item)
heapq.heappop(heap)
```

### Option 2: Import specific functions
```python
from heapq import heappush, heappop, heapify
heappush(heap, item)
heappop(heap)
```

### Option 3: Import all functions (Not recommended)
```python
from heapq import *
heappush(heap, item)
heappop(heap)
```

## Core Operations

### Basic Heap Operations

| Operation | Function | Time Complexity | Description |
|-----------|----------|----------------|-------------|
| **Create heap** | `heap = []` | O(1) | Create empty heap (just a list) |
| **Heapify** | `heapq.heapify(list)` | O(n) | Transform list into heap in-place |
| **Push** | `heapq.heappush(heap, item)` | O(log n) | Add item to heap |
| **Pop** | `heapq.heappop(heap)` | O(log n) | Remove and return smallest item |
| **Peek** | `heap[0]` | O(1) | Get smallest item without removing |
| **Push-Pop** | `heapq.heappushpop(heap, item)` | O(log n) | Push item, then pop smallest |
| **Replace** | `heapq.heapreplace(heap, item)` | O(log n) | Pop smallest, then push item |

### Advanced Operations

| Operation | Function | Time Complexity | Description |
|-----------|----------|----------------|-------------|
| **N Largest** | `heapq.nlargest(n, iterable)` | O(n + k log n) | Return n largest elements |
| **N Smallest** | `heapq.nsmallest(n, iterable)` | O(n + k log n) | Return n smallest elements |
| **Merge** | `heapq.merge(*iterables)` | O(k log k) | Merge k sorted iterables |

## Key Syntax Points

### 1. **Min-Heap Only**
```python
# Python heapq is ALWAYS a min-heap
heap = [1, 3, 2, 7, 5, 4]
heapq.heapify(heap)
print(heap[0])  # Always the minimum element
```

### 2. **Creating Max-Heap Workaround**
```python
# For max-heap, negate values
max_heap = []
heapq.heappush(max_heap, -5)  # Push -5 to simulate max-heap
heapq.heappush(max_heap, -3)  # Push -3
max_val = -heapq.heappop(max_heap)  # Pop and negate to get max
```

### 3. **Heap with Custom Objects**
```python
import heapq

# Using tuples (priority, item)
heap = []
heapq.heappush(heap, (2, 'task_b'))
heapq.heappush(heap, (1, 'task_a'))
heapq.heappush(heap, (3, 'task_c'))

priority, task = heapq.heappop(heap)  # Returns (1, 'task_a')
```

### 4. **Common Pitfalls**
```python
# ❌ Wrong: Don't mix import styles
from heapq import *
heapq.heappush(heap, item)  # NameError!

# ✅ Correct: Choose one style
import heapq
heapq.heappush(heap, item)

# ❌ Wrong: Don't use regular list operations
heap.append(item)  # Breaks heap property!

# ✅ Correct: Use heap operations
heapq.heappush(heap, item)
```

## Common LeetCode Patterns

### 1. **Top K Elements (Min-Heap)**
```python
import heapq

def top_k_frequent(nums, k):
    # Count frequencies
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Min-heap of size k
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Extract results
    return [num for freq, num in heap]
```

### 2. **Top K Elements (Max-Heap)**
```python
import heapq

def top_k_frequent_max_heap(nums, k):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Max-heap using negative values
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (-freq, num))
    
    # Extract top k
    result = []
    for _ in range(k):
        neg_freq, num = heapq.heappop(heap)
        result.append(num)
    
    return result
```

### 3. **Merge K Sorted Lists**
```python
import heapq

def merge_k_sorted_lists(lists):
    heap = []
    result = []
    
    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result
```

### 4. **Kth Largest Element**
```python
import heapq

def find_kth_largest(nums, k):
    # Min-heap of size k
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]  # Kth largest is the minimum in heap of size k
```

## Performance Comparison

### When to Use Each Operation

| Use Case | Best Operation | Alternative | Why |
|----------|---------------|-------------|-----|
| **Find top k** | `heapq` with size k | `nlargest(k)` | O(n log k) vs O(n log n) |
| **Priority queue** | `heapq.heappush/pop` | `queue.PriorityQueue` | Faster, no thread safety |
| **Streaming data** | `heapq.heappush/pop` | Sorting | Maintains order incrementally |
| **One-time top k** | `heapq.nlargest(k)` | Manual heap | Optimized for single use |

## Memory Considerations

### Space Complexity
- **Heap storage**: O(n) where n is number of elements
- **Heapify**: O(1) additional space (in-place)
- **Operations**: O(1) additional space

### Heap vs Other Data Structures

| Data Structure | Insert | Delete Min | Find Min | Use Case |
|---------------|--------|------------|----------|----------|
| **Heap** | O(log n) | O(log n) | O(1) | Priority queue, top k |
| **Sorted List** | O(n) | O(1) | O(1) | Static data |
| **BST** | O(log n) | O(log n) | O(log n) | Dynamic sorted data |

## Common Mistakes

### 1. **Forgetting Min-Heap Nature**
```python
# ❌ Wrong assumption
heap = [1, 5, 3, 9, 6, 8]
heapq.heapify(heap)
print(heap)  # [1, 5, 3, 9, 6, 8] - not sorted!

# ✅ Correct understanding
print(heap[0])  # 1 - guaranteed minimum
```

### 2. **Modifying Heap Directly**
```python
# ❌ Wrong
heap = [1, 3, 2]
heap.append(0)  # Breaks heap property!

# ✅ Correct
heapq.heappush(heap, 0)
```

### 3. **Not Handling Empty Heap**
```python
# ❌ Wrong
heap = []
min_val = heapq.heappop(heap)  # IndexError!

# ✅ Correct
if heap:
    min_val = heapq.heappop(heap)
```

## Edge Cases

### Empty Heap
```python
heap = []
# heapq.heappop(heap)  # IndexError
# heap[0]              # IndexError

# Safe operations
if heap:
    min_val = heap[0]
```

### Single Element
```python
heap = [5]
heapq.heappush(heap, 3)  # [3, 5]
print(heapq.heappop(heap))  # 3
```

### Duplicate Elements
```python
heap = [1, 1, 1, 2, 2]
heapq.heapify(heap)  # Works fine with duplicates
```

## Best Practices

1. **Use `import heapq`** for clarity
2. **Always check for empty heap** before popping
3. **Use tuples for priority queues** with (priority, item)
4. **Remember it's a min-heap** - negate for max-heap behavior
5. **Don't modify heap directly** - use heap operations
6. **Consider `nlargest/nsmallest`** for one-time operations

## Summary

- **heapq** provides efficient min-heap operations
- **Time complexity**: O(log n) for push/pop, O(1) for peek
- **Space complexity**: O(n) for storage
- **Key insight**: Perfect for top-k problems and priority queues
- **Remember**: It's always a min-heap, use negation for max-heap behavior