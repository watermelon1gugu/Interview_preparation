class Solution:
    def corpFlightBookings(self, bookings, n: int):
        res = [0 for _ in range(n)]
        for left, right, inc in bookings:
            res[left - 1] += inc
            if right < n:
                res[right] -= inc
        for i in range(1, len(res)):
            res[i] += res[i - 1]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))
