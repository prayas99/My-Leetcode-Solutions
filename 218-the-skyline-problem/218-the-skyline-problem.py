class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        from heapq import heappush, heappop
        buildings = sorted([(L, -H, R) for L, R, H in buildings] + [(R, 0, -1) for _, R, _ in buildings])
        result, heap = [(0, 0)], [(0, float('inf'))]
        
        for left, neg_height, right in buildings:
            
            while left >= heap[0][1]:
                heappop(heap)
                
            if neg_height < 0:
                heappush(heap, (neg_height, right))
                
            curr_max = -heap[0][0]
            
            if curr_max != result[-1][1]:
                result.append((left, curr_max))
                
        return result[1:]