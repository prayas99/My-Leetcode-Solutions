class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = [0]*n
        
        lmaxi = 0
        for i in range(n):            
            water[i] = lmaxi
            lmaxi = max(lmaxi, height[i])
        
        rmaxi = 0
        for j in range(n - 1, -1, -1):            
            water[j] = max(min(water[j], rmaxi) - height[j], 0)
            rmaxi = max(rmaxi, height[j])
        
        return sum(water)