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

    def DFS(self, start_node, target_node):

        visited = set()
        steps = 0

        def visit(node, steps):
            steps += 1
            for child_node in self.vertices[node]:
                if child_node == target_node:
                    return f'Found node {child_node} via node {node} after {steps} steps.'
                if node not in visited:
                    visited.add(node)
                    visit(node, steps)

        visit(start_node, steps)

        return f'Unable to find node {target_node} after {steps} steps, having searched through: {visited}'

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
print(graph.DFS(1, 6))
