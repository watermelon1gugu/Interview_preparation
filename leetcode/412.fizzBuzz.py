class Solution:
    def fizzBuzz(self, n: int):
        res = []
        for i in range(1, n + 1):
            a = i % 3
            b = i % 5
            tmp = ""
            if a != 0 and b != 0:
                tmp = str(i)
            else:
                if a == 0:
                    tmp = "Fizz"
                if b == 0:
                    tmp += "Buzz"
            res.append(tmp)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(15))
