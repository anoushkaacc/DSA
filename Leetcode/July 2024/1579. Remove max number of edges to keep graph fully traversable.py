class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        auf = unionfind(n)
        buf = unionfind(n)
        res = 0
        for edge in edges:
            if edge[0] == 3:
                if auf.union(edge[1], edge[2]) == 1:
                    buf.union(edge[1], edge[2])
                    res += 1
            if auf.is_connected() and buf.is_connected():
                return len(edges) - res
        for edge in edges:
            if edge[0] == 1:
                res += auf.union(edge[1], edge[2])
            if edge[0] == 2:
                res += buf.union(edge[1], edge[2])
            if auf.is_connected() and buf.is_connected():
                return len(edges) - res
        return -1 
class unionfind:
    def __init__(self, n):
        self.parent = [0] * (n + 1)
        self.node_count = n
    def find(self, x):
        if self.parent[x] == 0 or self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 0
        self.parent[py] = px
        self.node_count -= 1
        return 1
    def is_connected(self):
        return self.node_count == 1       
        
