class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        while label >= 1:
            res.append(label)
            label //= 2
        res = res[::-1]
        b = len(res) % 2 == 0
        for i in range(len(res)):
            if i % 2 != b:
                temp = (2**i)
                res[i] -= temp
                res[i] = (temp - res[i] - 1)
                res[i] += temp
        return res
        