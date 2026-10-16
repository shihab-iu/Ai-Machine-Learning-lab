import heapq
graph = {
    "A": [("B",1), ("C",4)],
    "B": [("D",2), ("E",5)],
    "C": [("E",1)],
    "D": [("G",6)],
    "E": [("G",3)],
    "G": []
}
h = {"A":7, "B":6, "C":3, "D":6, "E":2, "G":0}
def astar(graph, start, goal, h):
    pq = [(h[start], 0, start, [start])]
    best_g = {start: 0}
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal:
            return path, g
        for nbr, cost in graph[node]:
            new_g = g + cost
            if new_g < best_g.get(nbr, float("inf")):
                best_g[nbr] = new_g
                new_f = new_g + h[nbr]
                heapq.heappush(pq, (new_f, new_g, nbr, path + [nbr]))
    return None, float("inf")
path, cost = astar(graph, "A", "G", h)
print("Path:", path)
print("Total cost:", cost)
