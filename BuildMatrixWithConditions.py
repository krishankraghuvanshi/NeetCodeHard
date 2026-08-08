class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        row_g = defaultdict(list)
        row_indeg = [0] * (k + 1)

        for x, y in rowConditions:
            row_g[x].append(y)
            row_indeg[y] += 1

        q = deque()    
        for i in range(1, k+1):
            if row_indeg[i] == 0:
                q.append(i)

        row_order = []        
        while len(q) > 0:
            K = len(q)
            while K > 0:
                r = q.popleft()
                row_order.append(r)
                for nei in row_g[r]:
                    row_indeg[nei] -= 1
                    if row_indeg[nei] == 0:
                        q.append(nei)
                K -= 1        


        col_g = defaultdict(list) 
        col_indeg = [0] * (k + 1) 

        for x, y in colConditions:
            col_g[x].append(y)
            col_indeg[y] += 1

        for i in range(1, k+1):
            if col_indeg[i] == 0:
                q.append(i)

        col_order = []   

        while len(q) > 0:
            K = len(q)
            while K > 0:
                r = q.popleft()
                col_order.append(r)
                for nei in col_g[r]:
                    col_indeg[nei] -= 1
                    if col_indeg[nei] == 0:
                        q.append(nei) 
                K -= 1       


        row_dict, col_dict = defaultdict(int), defaultdict(int)

        print(row_order, col_order)

        if len(row_order) != len(col_order) or (len(row_order) == 0 or len(col_order) == 0):
            return []

        for i in range(len(row_order)):
            row_dict[row_order[i]] = i
        for i in range(len(col_order)):    
            col_dict[col_order[i]] = i

        ans = [[0] * k for _ in range(k)]

        for i in range(1, k+1):
            ans[row_dict[i]][col_dict[i]] = i
        return ans  

        '''
        c = [3, 2, 1] 
        r = [1, 3, 2]
        1 => 0, 2
        2 => 2, 1
        3 => 1, 0

        0, 0, 1
        3, 0, 0
        0, 2, 0
        
        CRAZY
        ''' 
