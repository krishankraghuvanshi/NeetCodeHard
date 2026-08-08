class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def is_valid(target):
            if grid[0][0] <= target:
                seen = [[False] * len(grid[0]) for _ in range(len(grid))]
                def dfs(x, y):
                    seen[x][y] = True
                    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if ((0 <= nx < len(grid) and 0 <= ny < len(grid[0])) and (not seen[nx][ny]) and (grid[nx][ny] <= target)):
                            dfs(nx, ny)
                dfs(0, 0)            
                return seen[len(grid)-1][len(grid[0])-1]
            else:
                return False    
        left = 1
        right = max(grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])))  
        ans = right 
        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                print(mid)
                right = mid-1
                ans = mid
            else:
                left = mid+1   
        return ans          

        
