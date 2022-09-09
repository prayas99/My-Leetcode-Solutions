class Solution:
    def twoEggDrop(self, n: int) -> int:
        i = 1
        while i*(i+1)//2<n:
            i += 1
        return i
        