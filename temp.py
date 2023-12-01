import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {v: [] for v in vertices}

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self, start_vertex):
        priority_queue = [(0, start_vertex)]  # (key, vertex)
        visited = {v: False for v in self.vertices}
        mst_cost = 0

        while priority_queue:
            key, u = heapq.heappop(priority_queue)

            if visited[u]:
                continue

            visited[u] = True
            mst_cost += key

            for v, weight in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(priority_queue, (weight, v))

        return mst_cost

# Example usage:
vertices = ['s', 'a', 'b', 'c', 'd', 'e']
g = Graph(vertices)
g.add_edge('s', 'a', 12)
g.add_edge('s', 'c', 20)
g.add_edge('s', 'e', 6)
g.add_edge('a', 'c', 4)
g.add_edge('b', 'c', 5)
g.add_edge('b', 'd', 7)
g.add_edge('c', 'd', 6)
g.add_edge('c', 'e', 2)
g.add_edge('d', 'e', 8)

start_vertex = 's'
mst_cost = g.prim_mst(start_vertex)
print(f"Minimum Spanning Tree Cost starting from vertex {start_vertex}: {mst_cost}")
