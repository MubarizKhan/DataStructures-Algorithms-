class digraph:
    def __init__(self):
        self.g = {}

    def add_node(self, node):
        if node in self.g:
            raise ValueError("Node already exists")

        self.g[node] = []

    def add_edge(self, src, dest):
        if src not in self.g:
            raise ValueError("Source doesn't exist in the graph")

        if dest not in self.g:
            raise ValueError("Destination doesn't exist in the graph")

        if dest in self.g[src]:
            return

        self.g[src].append(dest)
    
    def traverse_graph(self, start):
        q = [start]
        visited = []

        while q:
            current = q.pop(0)
            if current in visited:
                continue

            print(current)

            visited.append(current)

            next_nodes = self.g[start]

            for n in next_nodes:
                q.append(n)




obj = digraph()
list = ['a', 'b', 'c','d','e','f']
for n in list:
    obj.add_node(n)

edges = [
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'c'),
    ('b', 'd'),
    ('c', 'd'),
    ('d', 'c'),
    ('e', 'f'),
    ('f', 'c')
]

for n in edges:
    obj.add_edge(n[0], n[1])

obj.traverse_graph('b')






            