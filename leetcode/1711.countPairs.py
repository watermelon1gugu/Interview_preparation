class Solution:
    def check(self, num):
        return str(bin(num)).count("1") == 1

    def countPairs(self, deliciousness) -> int:
        MOD = 10 ** 9 + 7
        m = {}
        res = 0
        for item in deliciousness:
            if item not in m:
                m[item] = 1
            else:
                m[item] += 1

        items = list(m.items())
        for i in range(len(items)):
            if items[i][1] > 1 and self.check(items[i][0]):
                n = items[i][1] - 1
                res += n * n - int(n * (n - 1) / 2)
                res = res % MOD
            for j in range(i + 1, len(items)):
                if self.check(items[i][0] + items[j][0]):
                    res += items[i][1] * items[j][1]
                    res = res % MOD
        return res

if __name__ == '__main__':
    print(4/2)
