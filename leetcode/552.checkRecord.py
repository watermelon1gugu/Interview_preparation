class Solution:
    def checkRecord(self, n: int) -> int:
        res = 0
        MOD = 10 ** 9 + 7
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1
        for day in range(1, n + 1):
            dp[day][0][0] = (dp[day - 1][0][0] + dp[day - 1][0][1] + dp[day - 1][0][2]) % MOD
            dp[day][1][0] = (dp[day - 1][0][0] + dp[day - 1][1][0] + dp[day - 1][0][2] + dp[day - 1][1][2] + \
                             dp[day - 1][0][1] + dp[day - 1][1][1]) % MOD
            dp[day][0][1] = dp[day - 1][0][0]
            dp[day][1][1] = dp[day - 1][1][0]
            dp[day][0][2] = dp[day - 1][0][1]
            dp[day][1][2] = dp[day - 1][1][1]
        for i in range(2):
            for j in range(3):
                res += dp[n][i][j]
                res %= MOD
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.checkRecord(100000))
