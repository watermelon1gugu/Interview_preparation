class Solution:
    def countArrangement(self, n: int) -> int:
        m = {i: [] for i in range(1, n + 1)}
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if j % i == 0 or i % j == 0:
                    m[i].append(j)
        vis = set()
        num = 0

        def dfs(index):
            if index == n + 1:
                nonlocal num
                num += 1
                return
            for x in m[index]:
                if x not in vis:
                    vis.add(x)
                    dfs(index + 1)
                    vis.discard(x)

        dfs(1)
        return num


if __name__ == '__main__':
    s = Solution()
    for i in range(1, 30):
        print(f"{i}:{s.countArrangement(i)}")
