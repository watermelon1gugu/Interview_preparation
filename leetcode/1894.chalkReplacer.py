class Solution:
    def chalkReplacer(self, chalk, k: int) -> int:
        n = sum(chalk)
        k = k % n
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]


if __name__ == '__main__':
    s = Solution()
    print(s.chalkReplacer(chalk=[3, 4, 1, 2], k=25))
