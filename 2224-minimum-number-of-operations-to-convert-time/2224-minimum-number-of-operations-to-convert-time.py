class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        c_h, c_m = int(current[:2]), int(current[-2:])
        t_h, t_m = int(correct[:2]), int(correct[-2:])
        tar = t_h*60 + t_m - c_h*60 - c_m
        res = 0
        for step in [60, 15, 5, 1]:
            if tar > 0:
                res += tar// step
                tar %= step
        return res