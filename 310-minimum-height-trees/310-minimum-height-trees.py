class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        indeg = defaultdict(int)
        for x, y in edges:
            adj[x].append(y)
            indeg[x] += 1
            adj[y].append(x)
            indeg[y] += 1
        leaves = [k for k, v in indeg.items() if v == 1]
        visi = set(leaves)


        q = deque(leaves)
        while q:
            if n <= 2:
                return q
            for _ in range(len(q)):
                node = q.popleft()
                n -= 1
                for child in adj[node]:
                    if child in visi:
                        continue
                    indeg[child] -= 1
                    if indeg[child] == 1:
                        q.append(child)
                        visi.add(child)
