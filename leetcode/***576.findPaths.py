class Solution:

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        dp[0][startRow][startColumn] = 1
        count = 0
        for move in range(0, maxMove):
            for row in range(m):
                for col in range(n):
                    for row1, col1 in [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]:
                        if 0 <= row1 < m and 0 <= col1 < n:
                            dp[move + 1][row1][col1] = (dp[move + 1][row1][col1] + dp[move][row][col]) % MOD
                        else:
                            count = (count + dp[move][row][col]) % MOD
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.findPaths(2, 2, 2, 0, 0))
