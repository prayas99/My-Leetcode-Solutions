class Solution:
    def minimumBuckets(self, street: str) -> int:
        street = [c for c in street]
        street.insert(0, 'H')
        street.append('H')
        res = 0
        for i in range(1, len(street) - 1):
            if street[i] == 'H':
                if street[i + 1] == 'B' or street[i - 1] == 'B':
                    continue
                if street[i + 1] == '.':
                    street[i + 1] = 'B'
                    res += 1
                elif street[i - 1] == '.':
                    res += 1
                else:
                    return -1
        return res
        
                    
        