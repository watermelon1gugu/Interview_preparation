import random

rand_n = 7


class Solution:
    cache = 0
    upper = 1

    def rand10(self):
        while self.upper < 10 ** 9:  # 这里似乎可以为10的任何一个次方
            self.cache = self.cache * 7 + rand7() - 1
            self.upper *= 7
        res = self.cache % 10 + 1
        self.cache, self.upper = self.cache // 10, self.upper // 10
        return res


def rand7():
    return random.randint(1, 7)


def rand(n):
    return random.randint(1, n)


if __name__ == '__main__':
    s = Solution()
    count = 10
    m = {i: 0 for i in range(1, 11)}
    for _ in range(count):
        m[s.rand10()] += 1
    print(m)
