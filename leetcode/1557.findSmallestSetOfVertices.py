class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        s = set()
        for edge in edges:
            s.add(edge[1])
        res = []
        for i in range(n):
            if i not in s:
                res.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findSmallestSetOfVertices(5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))
