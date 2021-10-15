class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num += 16 ** 8

        book = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        res = ""
        base = 16
        while True:
            remainder = num % base
            res = book[remainder] + res
            if num >= base:
                num -= remainder
                num //= base
            else:
                break
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.toHex(-1))
