class Solution:
    def get_min(self, num: int):
        s = str(num)
        for i in range(len(s)):
            if i != 0 and s[i] != s[0]:
                y = "0"
            else:
                y = "1"

            if s[i] != y:
                s = s.replace(s[i], y)
                return int(s)
        return num

    def get_max(self, num: int):
        s = str(num)
        for i in range(len(s)):
            if s[i] != "9":
                s = s.replace(s[i], "9")
                return int(s)
        return num

    def maxDiff(self, num: int) -> int:
        return self.get_max(num) - self.get_min(num)


if __name__ == '__main__':
    s = Solution()
    print(s.maxDiff(1101057))
