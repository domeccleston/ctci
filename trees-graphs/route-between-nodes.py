class Graph:
    def __init__(self):
        self.vertices = {}

    def add_node(self, node):
        self.vertices[node] = set()

    def add_nodes(self, nodes):
        for i in nodes:
            self.add_node(i)

    def add_edge(self, nodeA, nodeB):
        self.vertices[nodeA].add(nodeB)

    def DFS(self, node, visited=set()):
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbour in self.vertices[node]:
                self.DFS(neighbour, visited)

    def BFS(self, node):
        visited = set()
        queue = []

        queue.append(node)
        visited.add(node)
        
        while queue:
            head = queue.pop(0)
            print(head)

            for adjacent_node in self.vertices[node]:
                if not adjacent_node in visited:
                    queue.append(adjacent_node)
                    visited.add(adjacent_node)

    def __repr__(self):
        return str(self.vertices)


graph = Graph()
graph.add_nodes([1, 2, 3, 4, 5, 6])
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(4, 2)
graph.add_edge(4, 5)
graph.add_edge(5, 6)
print(graph.DFS(1))
