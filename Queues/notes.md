
## Queue Operations: Time Complexity

| Operation      | Time Complexity |
|---------------|----------------|
| Enqueue       | O(1)           |
| Dequeue       | O(1)           |
| Front/Peek    | O(1)           |
| isEmpty       | O(1)           |
| Size/Length   | O(1)           |

---

## Key Leetcode / Coding Assessment Patterns for Queues

- **Breadth-First Search (BFS) in Trees/Graphs**
  - e.g., "Binary Tree Level Order Traversal", "Word Ladder"
- **Sliding Window Problems**
  - e.g., "Sliding Window Maximum", "First Negative Integer in Every Window of Size K"
- **Order Processing / Simulation**
  - e.g., "Design Hit Counter", "Number of Recent Calls"
- **Round Robin Scheduling / Task Processing**
  - e.g., "Rotting Oranges", "Dota2 Senate"
- **Shortest Path in Unweighted Graphs**
  - e.g., "Shortest Path in Binary Matrix"
- **Multi-source BFS**
  - e.g., "Walls and Gates"
- **Stream Processing**
  - e.g., "Moving Average from Data Stream"

**Tip:** Queues are ideal for problems that require processing elements in the order they arrive (FIFO), or when you need to explore neighbors level by level (as in BFS).

**How to Recognize Queue Patterns:**
- The problem requires visiting nodes or elements in "layers" or "levels" (e.g., level order traversal).
- You need to process items in the order they were added, without skipping any.
- The solution involves a "first in, first out" (FIFO) order.
- The problem involves simulating real-world queues (e.g., customer service, task scheduling).
- The problem asks for the shortest path or minimum number of steps in an unweighted graph.
- You need to maintain a window or range of elements and process them as a group.

If you see these cues, consider whether a queue (or double-ended queue, deque) could help structure your solution!

---

## Python Queue vs Deque: Key Method Differences

### Queue (from queue module)
```python
from queue import Queue

q = Queue()
q.put(item)      # Add to end
q.get()          # Remove from front (FIFO)
q.empty()        # Check if empty
q.qsize()        # Get size
q.full()         # Check if full (if maxsize set)
```

### Deque (from collections module)
```python
from collections import deque

d = deque()
d.append(item)           # Add to end
d.appendleft(item)       # Add to front
d.pop()                  # Remove from end
d.popleft()              # Remove from front
d[0]                     # Access front element
d[-1]                    # Access back element
len(d)                   # Get size
d.clear()                # Clear all elements
d.extend(iterable)       # Add multiple items to end
d.extendleft(iterable)   # Add multiple items to front
d.rotate(n)              # Rotate elements by n positions
```

### Key Differences:
- **Queue**: Thread-safe, designed for producer-consumer scenarios
- **Deque**: Not thread-safe, but more flexible with O(1) operations on both ends
- **Queue**: Only FIFO operations (put/get)
- **Deque**: Supports both ends efficiently (append/pop/appendleft/popleft)
- **Queue**: Has size limits and blocking operations
- **Deque**: No size limits, more like a list with efficient ends

**When to use which:**
- Use **Queue** for multi-threaded applications or when you need thread safety
- Use **Deque** for single-threaded applications where you need efficient operations on both ends