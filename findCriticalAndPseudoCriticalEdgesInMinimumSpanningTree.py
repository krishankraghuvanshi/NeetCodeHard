class union_find:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def ufind(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.ufind(self.parent[u])
        return self.parent[u]
    def uunion(self, u, v):
        self.parent[self.ufind(v)] = self.parent[self.ufind(u)]  

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def calculate_mst():
            uf = union_find(n)
            sorted_edges = sorted(edges, key=lambda x: x[2])
            weight = 0
            count = 0
            for u, v, w in sorted_edges:
                if count == n-1:
                    break
                if uf.ufind(u) != uf.ufind(v):
                    weight += w
                    count += 1
                    uf.uunion(u, v)
            return weight

        mst_weight = calculate_mst()
        def check_critical(uu, vv, ww, required):
            uf = union_find(n)
            sorted_edges = sorted(edges, key=lambda x: x[2])
            weight = 0
            count = 0
            for u, v, w in sorted_edges:
                if (uu, vv, ww) == (u, v, w):
                    continue
                if count == n-1:
                    break
                if uf.ufind(u) != uf.ufind(v):
                    weight += w
                    count += 1
                    uf.uunion(u, v)
            return weight != required

        def check_p_critical(uu, vv, ww, required):
            uf = union_find(n)
            sorted_edges = sorted(edges, key=lambda x: x[2])
            weight = 0
            count = 0
            if uf.ufind(uu) != uf.ufind(vv):
                weight += ww
                count += 1
                uf.uunion(uu, vv)

            for u, v, w in sorted_edges:
                if (uu, vv, ww) == (u, v, w):
                    continue
                if count == n-1:
                    break
                if uf.ufind(u) != uf.ufind(v):
                    weight += w
                    count += 1
                    uf.uunion(u, v)
            return weight == required 

        critical = []    
        visited = set()
        for i, (uu, vv, ww) in enumerate(edges):
            if check_critical(uu, vv, ww, mst_weight):
                visited.add(i)
                critical.append(i)

        p_critical = []        
        for i, (uu, vv, ww) in enumerate(edges):
            if i not in visited:
                if check_p_critical(uu, vv, ww, mst_weight):
                    p_critical.append(i)

        return [critical, p_critical]            
