import heapq


class Solution:
    def smallestK(self, arr, k: int):
        return heapq.nsmallest(k, arr)


if __name__ == '__main__':
    s = Solution()
    print(s.smallestK( [6, 5, 4, 3, 2, 1],3))
