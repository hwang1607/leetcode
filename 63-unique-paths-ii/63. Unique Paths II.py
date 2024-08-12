class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        paths = 0
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        dp = {(ROWS-1, COLS-1): 1} #bottom right is 1

        def dfs(r,c):
            if r >= ROWS or c >= COLS or obstacleGrid[r][c] == 1:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            dp[(r,c)] =  dfs(r+1, c) + dfs(r, c+1)
            return dp[(r,c)]
            
        
        return dfs(0,0)
        
        return paths