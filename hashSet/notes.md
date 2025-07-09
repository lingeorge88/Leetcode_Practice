# Python Set Operations & Time Complexities

## Common Set Operations

### Basic Operations
| Operation | Syntax | Time Complexity | Description |
|-----------|--------|----------------|-------------|
| **Creation** | `set()` or `{1, 2, 3}` | O(n) | Create empty set or from iterable |
| **Add element** | `s.add(x)` | O(1) average | Add single element |
| **Remove element** | `s.remove(x)` | O(1) average | Remove element (raises KeyError if not found) |
| **Discard element** | `s.discard(x)` | O(1) average | Remove element (no error if not found) |
| **Pop element** | `s.pop()` | O(1) average | Remove and return arbitrary element |
| **Clear all** | `s.clear()` | O(n) | Remove all elements |

### Lookup Operations
| Operation | Syntax | Time Complexity | Description |
|-----------|--------|----------------|-------------|
| **Membership test** | `x in s` | O(1) average | Check if element exists |
| **Size** | `len(s)` | O(1) | Get number of elements |
| **Is empty** | `len(s) == 0` | O(1) | Check if set is empty |

### Set Theory Operations
| Operation | Syntax | Time Complexity | Description |
|-----------|--------|----------------|-------------|
| **Union** | `s1 \| s2` or `s1.union(s2)` | O(len(s1) + len(s2)) | Elements in either set |
| **Intersection** | `s1 & s2` or `s1.intersection(s2)` | O(min(len(s1), len(s2))) | Elements in both sets |
| **Difference** | `s1 - s2` or `s1.difference(s2)` | O(len(s1)) | Elements in s1 but not s2 |
| **Symmetric difference** | `s1 ^ s2` or `s1.symmetric_difference(s2)` | O(len(s1) + len(s2)) | Elements in either set but not both |
| **Subset test** | `s1 <= s2` or `s1.issubset(s2)` | O(len(s1)) | Check if s1 is subset of s2 |
| **Superset test** | `s1 >= s2` or `s1.issuperset(s2)` | O(len(s2)) | Check if s1 is superset of s2 |

### In-Place Operations
| Operation | Syntax | Time Complexity | Description |
|-----------|--------|----------------|-------------|
| **Update** | `s1.update(s2)` or `s1 \|= s2` | O(len(s2)) | Add all elements from s2 to s1 |
| **Intersection update** | `s1.intersection_update(s2)` or `s1 &= s2` | O(len(s1)) | Keep only common elements |
| **Difference update** | `s1.difference_update(s2)` or `s1 -= s2` | O(len(s2)) | Remove elements that are in s2 |

## LeetCode Patterns Where Sets Are Useful

### 1. **Duplicate Detection**
**Pattern**: Find duplicates, remove duplicates, or check for uniqueness
```python
# Example: Contains Duplicate
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
```
**Problems**: Contains Duplicate, Remove Duplicates, Find the Duplicate Number

### 2. **Fast Lookup/Membership Testing**
**Pattern**: Need to check if element exists in O(1) time
```python
# Example: Two Sum
def twoSum(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
```
**Problems**: Two Sum, 3Sum, Valid Anagram, Group Anagrams

### 3. **Set Operations for Array Problems**
**Pattern**: Finding intersection, union, or difference between collections
```python
# Example: Intersection of Two Arrays
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
```
**Problems**: Intersection of Arrays, Find Common Characters, Set Mismatch

### 4. **Tracking Visited Elements**
**Pattern**: Mark elements as visited during traversal (DFS/BFS, graphs)
```python
# Example: Number of Islands (DFS)
def numIslands(grid):
    visited = set()
    # ... DFS logic using visited.add((row, col))
```
**Problems**: Number of Islands, Word Search, Clone Graph, Course Schedule

### 5. **Sliding Window with Unique Elements**
**Pattern**: Maintain window of unique elements
```python
# Example: Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```
**Problems**: Longest Substring Without Repeating Characters, Fruit Into Baskets

### 6. **Finding Missing or Extra Elements**
**Pattern**: Compare what should be present vs what is present
```python
# Example: Missing Number
def missingNumber(nums):
    expected = set(range(len(nums) + 1))
    actual = set(nums)
    return list(expected - actual)[0]
```
**Problems**: Missing Number, Find All Numbers Disappeared in Array, Single Number

### 7. **Cycle Detection**
**Pattern**: Use set to detect if we've seen a state before
```python
# Example: Linked List Cycle
def hasCycle(head):
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False
```
**Problems**: Linked List Cycle, Happy Number, Word Ladder

### 8. **Counting Unique Elements**
**Pattern**: Need to count distinct elements or characters
```python
# Example: Unique Email Addresses
def numUniqueEmails(emails):
    unique_emails = set()
    for email in emails:
        # ... email processing logic
        unique_emails.add(processed_email)
    return len(unique_emails)
```
**Problems**: Unique Email Addresses, Jewels and Stones, Unique Number of Occurrences

## Key Insights for LeetCode

1. **When to use sets**: When you need fast O(1) lookup, uniqueness constraints, or set theory operations
2. **Hash collision considerations**: Average case is O(1), but worst case can be O(n)
3. **Memory trade-off**: Sets use extra space for faster lookup times
4. **Immutable elements only**: Sets can only contain hashable (immutable) elements
5. **Order doesn't matter**: If you need to preserve order, consider using a list or OrderedDict instead

## Common Mistakes to Avoid

- Using sets when order matters (sets are unordered)
- Trying to add mutable objects (lists, dicts) to sets
- Forgetting that set operations create new sets (use in-place versions when needed)
- Not considering hash collision edge cases for worst-case time complexity