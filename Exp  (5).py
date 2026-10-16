tree = {
    "S": ["A", "B"],
    "A": ["C", "D"],
    "B": ["E", "F"],
    "C": [], "D": ["G"],
    "E": [], "F": [], "G": []
}
def depth_limited_search(graph, start, goal, limit):
    def rec(node, path, depth):
        if node == goal:
            return path
        if depth == limit:
            return None
        for nbr in graph[node]:
            if nbr not in path:
                result = rec(nbr, path + [nbr], depth + 1)
                if result:
                    return result
        return None
    return rec(start, [start], 0)
def iddfs(graph, start, goal, max_depth=10):
    for limit in range(max_depth + 1):
        result = depth_limited_search(graph, start, goal, limit)
        if result:
            return limit, result
    return None, None
print("DLS limit 2:", depth_limited_search(tree, "S", "G", 2))
print("DLS limit 3:", depth_limited_search(tree, "S", "G", 3))
print("IDDFS:", iddfs(tree, "S", "G", 5))