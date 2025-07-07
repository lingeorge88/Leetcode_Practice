## Stack Operations: Time Complexity

| Operation      | Time Complexity |
|---------------|----------------|
| Push          | O(1)           |
| Pop           | O(1)           |
| Top/Peek      | O(1)           |
| isEmpty       | O(1)           |
| Size/Length   | O(1)           |

---

## Key Leetcode / Coding Assessment Patterns for Stacks

- **Balanced Parentheses / Valid Brackets**
  - e.g., "Valid Parentheses", "Longest Valid Parentheses"
- **Next Greater/Smaller Element**
  - e.g., "Next Greater Element I/II", "Daily Temperatures"
- **Monotonic Stack Problems**
  - e.g., "Largest Rectangle in Histogram", "Trapping Rain Water"
- **Reverse Data (Strings, Linked Lists, etc.)**
  - e.g., "Reverse Polish Notation", "Reverse Linked List" (sometimes)
- **Backtracking with Undo Operations**
  - e.g., "Simplify Path", "Min Stack"
- **DFS Iterative Implementations**
  - e.g., "Binary Tree Preorder Traversal" (iterative)
- **Span Problems**
  - e.g., "Stock Span Problem"
- **Undo/Redo Functionality**
  - e.g., Text editor simulations
- **Expression Evaluation**
  - e.g., "Evaluate Reverse Polish Notation"

**Tip:** If a problem involves nested structures, matching pairs, or requires remembering the order of elements for later processing, a stack is often the optimal data structure.

**How to Recognize Stack Patterns:**
- The problem asks to check for balanced or properly nested symbols (parentheses, brackets, tags).
- You need to process elements in reverse order or "undo" previous actions.
- The problem involves finding the next/previous greater or smaller element for each item in a list.
- You need to maintain a history of operations or states (e.g., browser history, text editor undo/redo).
- The solution requires evaluating or parsing expressions (infix, postfix, prefix notation).
- The problem involves traversing a tree or graph iteratively (especially DFS).
- You need to keep track of indices or positions while scanning through an array or string, especially for range or span calculations.
- The problem hints at "last in, first out" (LIFO) behavior, or you need to access the most recent unprocessed element.

If you see any of these cues in a problem statement, consider whether a stack could simplify your solution!

