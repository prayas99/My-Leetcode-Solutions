class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        prv = [poured]
        while True:
            if len(prv) == query_row + 1:
                return min(prv[query_glass], 1)
            
            curr = [0]*(len(prv) + 1)
            b = 1
            for i in range(len(curr)):
                if i == 0:
                    curr[i] = max((prv[i] - 1)/2, 0)
                elif i == len(curr) - 1:
                    curr[i] = max((prv[-1] - 1)/2, 0)
                else:
                    curr[i] = max((prv[i - 1] - 1)/2, 0) + max((prv[i] - 1)/2,0)
                if curr[i] != 0:
                    b = 0
            if b:
                return 0
            prv = curr
        
