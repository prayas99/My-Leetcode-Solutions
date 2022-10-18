class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0]*(n + 1)
        for i, j, s in bookings:
            arr[i - 1] += s
            arr[j + 1 - 1] -= s
        for i in range(1, n + 1):
            arr[i] += arr[i - 1]
        arr.pop()
        return arr