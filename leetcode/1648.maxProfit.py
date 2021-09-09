class Solution:
    def maxProfit(self, inventory, orders: int) -> int:
        MOD = 10 ** 9 + 7
        inventory.sort(reverse=True)
        inventory.append(0)
        base = 1
        need = orders
        res = 0
        for i in range(len(inventory)):
            n = inventory[i] - inventory[i + 1]
            if n * base < need:
                cc = n * (n - 1) % MOD
                res += base * (n * inventory[i] % MOD - int(cc / 2))% MOD
                res = res % MOD
                need -= base * n
                base += 1
            else:
                n = int(need / base)
                cc = n * (n - 1) % MOD
                res += base * (n * inventory[i] % MOD - int(cc / 2))% MOD
                res += need % base * (inventory[i] - n) % MOD
                res = res % MOD
                break
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([773160767], 252264991))
