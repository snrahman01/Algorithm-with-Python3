from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.parent = [-1] * (self.V)
        self.sz = [0]*(self.V)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def find_parent(self,  i):
        if self.parent[i] == -1:
            return i
        if self.parent[i] != -1:
            return self.find_parent(self.parent[i])

    def union(self, x, y):
        x_set = self.find_parent(x)
        y_set = self.find_parent(y)
        if self.sz[x_set] < self.sz[y_set]:
            self.parent[x_set] = y_set
            self.sz[y_set] += self.sz[x_set]
        else:
            self.parent[y_set] = x_set
            self.sz[x_set] += self.sz[y_set]

    def isCyclic(self):
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(i)
                y = self.find_parent(j)
                if x == y:
                    return True
                self.union(x, y)

g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")

