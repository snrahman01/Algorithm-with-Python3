from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.parent = [-1] * (self.V)
        for i in range(self.V):
            self.parent[i] = i
        self.sz = [1]*(self.V)

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_parent(self,  i):
        if self.parent[i] == i:
            return i
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

    def KruskalMST(self):

        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_parent(u)
            y = self.find_parent(v)
            if x != y:
                self.union(x, y)
                e = e + 1
                result.append([u, v, w])

        print("Following are the edges in the constructed MST")
        for u, v, weight in result:
            print("%d -- %d == %d" % (u, v, weight))

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.KruskalMST()

