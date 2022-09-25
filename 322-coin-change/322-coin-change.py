class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        coins.sort(reverse=True)
        def bfs():
            layer, q = 1, deque([0])
            visited = set()
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    for coin in coins:
                        nexti = coin + curr
                        if nexti > amount or nexti in visited:
                            continue
                        if nexti == amount:
                            return layer
                        q.append(nexti)
                        visited.add(nexti)
                layer += 1
            return -1
        return bfs()
                        
                        
                        
                            