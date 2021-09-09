class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        res = 0
        for c in s:
            if c == "L":
                count += 1
            else:
                count -= 1
            if count == 0:
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.balancedStringSplit("RLLLLRRRLR"))
