class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r, c, visit, prevheight):
            if ((r,c) in visit or r < 0 or c < 0 or r == rows or c  == cols or heights[r][c] < prevheight):
                return
            
            visit.add((r,c))

            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(cols): #cols in first row, last row
            dfs(0, c, pac, heights[0][c])
            dfs(rows -1, c, atl, heights[rows-1][c])

        for r in range(rows): #left and right sides
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        # for r in range(rows):
        #     for c in range(cols):
        #         if (r,c) in pac and (r,c) in atl:
        #             res.append([r,c])
        
        # for x in pac:
        #     if x in atl:
        #         res.append(x)
        
        res = [x for x in pac if x in atl]

        return res

                
        