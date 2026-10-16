from collections import deque
import heapq
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "G"],
    "E": ["B", "G"],
    "F": ["C", "G"],
    "G": ["D", "E", "F"]
}
def bfs(graph, start, goal):
    q = deque([[start]])
    visited = {start}
    while q:
        path = q.popleft()
        node = path[-1]
        if node == goal:
            return path
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                q.append(path + [nbr])
def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for nbr in reversed(graph[node]):
                if nbr not in visited:
                    stack.append((nbr, path + [nbr]))
def bidirectional(graph, start, goal):
    if start == goal:
        return [start]
    qs, qg = deque([start]), deque([goal])
    ps, pg = {start:[start]}, {goal:[goal]}
    vs, vg = {start}, {goal}
    while qs and qg:
        for _ in range(len(qs)):
            node = qs.popleft()
            for nbr in graph[node]:
                if nbr not in vs:
                    vs.add(nbr); ps[nbr] = ps[node] + [nbr]; qs.append(nbr)
                    if nbr in vg:
                        return ps[nbr] + list(reversed(pg[nbr][:-1]))
        for _ in range(len(qg)):
            node = qg.popleft()
            for nbr in graph[node]:
                if nbr not in vg:
                    vg.add(nbr); pg[nbr] = pg[node] + [nbr]; qg.append(nbr)
                    if nbr in vs:
                        return ps[nbr] + list(reversed(pg[nbr][:-1]))
heuristic = {"A":6, "B":4, "C":4, "D":2, "E":2, "F":1, "G":0}
def greedy_best_first(graph, start, goal, h):
    pq = [(h[start], start, [start])]
    visited = set()
    while pq:
        _, node, path = heapq.heappop(pq)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                heapq.heappush(pq, (h[nbr], nbr, path + [nbr]))
print("BFS:", bfs(graph, "A", "G"))
print("DFS:", dfs(graph, "A", "G"))
print("Bidirectional:", bidirectional(graph, "A", "G"))
print("Greedy:", greedy_best_first(graph, "A", "G", heuristic))