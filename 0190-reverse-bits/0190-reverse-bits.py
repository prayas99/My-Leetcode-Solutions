class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if n & (1 << i):
                bit = 1
            else:
                bit = 0
            res |= (bit << (32 - i - 1))
        return res