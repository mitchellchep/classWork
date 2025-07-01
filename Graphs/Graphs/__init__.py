class Graphs:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_string = ""
        for node, neighbours in self.adj_list.items():
            graph_string += f"{node} -> {neighbours}\n"
        return graph_string

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists")

    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            self.adj_list[from_node].add(to_node)
            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add((to_node, weight))
            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    def obtain_neighbours(self, node):
        return self.adj_list.get(node, set())

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited and neighbour not in queue:
                        queue.append(neighbour)
        return order

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        stack.append(neighbour)
        return order

# 🧪 Main testing block
if __name__ == "__main__":
    # Directed graph
    graph_obj = Graphs(directed=True)

    graph_obj.add_edge(from_node="A", to_node="B", weight=2)
    graph_obj.add_edge(from_node="A", to_node="J", weight=2)
    graph_obj.add_edge(from_node="A", to_node="C", weight=3)
    graph_obj.add_edge(from_node="B", to_node="C", weight=4)
    graph_obj.add_edge(from_node="D", to_node="C", weight=5)

    print("Directed Graph:\n", graph_obj)
    print("BFS from A:", graph_obj.bfs("A"))
    print("DFS from A:", graph_obj.dfs("A"))

    print("\n" + "="*40 + "\n")

    # Undirected graph
    g = Graphs(directed=False)
    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 3)
    g.add_edge('B', 'D', 4)

    print("Undirected Graph:\n", g)
    print("BFS from A:", g.bfs('A'))
    print("DFS from A:", g.dfs('A'))
