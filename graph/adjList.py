class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = [] # O( V + E) space complexity


""" 
 We can use a hashmap where the key is a vertex and it maps to a list or array of its neighbors, which are also vertices. A hash map works here because we are assuming that all of the values keys are unique.
"""

# Or use a HashMap
adjList = { "A": [], "B": [] }

# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

adjList = {}

for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    
    adjList[src].append(dst)

# count paths O(V^2)
def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    # backtrack
    visit.remove(node)

    return count

# Shortest path from node to target O(V + E)
def bfs(node, target, adjList):
    length = 0
    visit = set()
    visit.add(node)
    queue = collections.deque()
    queue.append(node)

    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length

            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        length += 1
    return length