class Solution:

    def dfs(self, graph, now: list, res):
        if now[-1] == len(graph) - 1:
            res.append(now.copy())
        else:
            for target in graph[now[-1]]:
                now.append(target)
                self.dfs(graph, now, res)
                now.pop()

    def allPathsSourceTarget(self, graph):
        now = [0]
        res = []
        self.dfs(graph, now, res)
        return res


# [[4,3,1],[3,2,4],[3],[4],[]]


if __name__ == '__main__':
    s = Solution()
    print(s.allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))
