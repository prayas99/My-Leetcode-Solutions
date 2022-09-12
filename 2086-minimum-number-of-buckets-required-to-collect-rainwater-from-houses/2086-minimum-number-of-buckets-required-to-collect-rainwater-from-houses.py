class Solution:
    def minimumBuckets(self, street: str) -> int:
        street = [c for c in street]
        street.append('H')
        res = 0
        for i in range(len(street) - 1):
            if street[i] == 'H':
                if street[i + 1] == 'B' or street[i - 1] == 'B':
                    continue
                if street[i + 1] == '.':
                    street[i + 1] = 'B'
                    res += 1
                elif i > 0 and street[i - 1] == '.':
                    res += 1
                else:
                    return -1
        return res