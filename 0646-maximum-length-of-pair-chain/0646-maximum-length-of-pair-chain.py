class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x : x[1])
        
        count = 1
        b = pairs[0][1]
        
        for i in range(1, len(pairs)):
            if pairs[i][0] > b:
                count += 1
                b = pairs[i][1]
                
        return count