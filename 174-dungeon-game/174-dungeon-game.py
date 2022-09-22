class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        grid = [[(float('-inf'), float('-inf')) for _ in range(n + 1)] for _ in range(m + 1)]
        grid[-1][-2] = (0, 0)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                valc = dungeon[i][j]
                mina, vala = grid[i + 1][j]
                minb, valb = grid[i][j + 1]
                if mina > minb:
                    newval = vala + valc
                    grid[i][j] = (min(mina + valc, valc), newval)
                else:
                    newval = valb + valc
                    grid[i][j] = (min(minb + valc, valc), newval)
        return (-grid[0][0][0] + 1) if grid[0][0][0] < 0 else 1