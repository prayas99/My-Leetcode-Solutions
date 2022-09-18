class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = [0]*n
        
        lmaxi = 0
        for i in range(n):
            lmaxi = max(lmaxi, height[i])
            water[i] = lmaxi
        
        rmaxi = 0
        for j in range(n - 1, -1, -1):
            rmaxi = max(rmaxi, height[j])
            water[j] = min(water[j], rmaxi) - height[j]
        
        return sum(water)