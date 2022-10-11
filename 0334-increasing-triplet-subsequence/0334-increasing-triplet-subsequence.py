class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mini = float('inf')
        green = float('inf')
        # we just to find a number which has a number less than itself on its left and a number greater than it on right side
        # We can't see what's on right so we will just remember all "green" numbers where green number is such that it has a smaller number on its left, then we will check if current number is greater than green number
        for num in nums:
            if num > green:
                return True
            if mini < num:
                green = min(green, num)
            mini = min(mini, num)
        return