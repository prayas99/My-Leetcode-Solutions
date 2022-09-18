class Solution:
    def trap(self, height: List[int]) -> int:
        cur_max = height[0]
        l_sum = 0
        k = 0
        tval = 0
        for i,val in enumerate(height[1:]):
            i+=1
            if val>=cur_max:
                width = (i-k)-1
                tval+=(width*cur_max)-l_sum
                k = i
                l_sum = 0
                cur_max = val
            else:
                l_sum+=val
                
        l_sum = 0
        cur_max = height[-1]
        j = len(height)-1
        for i in range(len(height)-2, k-1, -1):
            if height[i]>=cur_max:
                width = (j-i)-1
                tval+=(width*cur_max)-l_sum
                j = i
                l_sum = 0
                cur_max = height[i]
            else:
                l_sum+=height[i]  
                
        return tval
                
                
        