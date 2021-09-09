class Solution:
    def isSelfCrossing(self, distance) -> bool:
        return len(distance) >= 4 and any(((distance[i] >= distance[i - 2] and distance[i - 3] >= distance[i - 1]) or (
                i >= 4 and distance[i - 1] == distance[i - 3] and distance[i] >= distance[i - 2] - distance[i - 4]) or (
                                                   i >= 5 and distance[i - 2] >= distance[i - 4] and distance[i - 3] >=
                                                   distance[i - 1] and distance[i - 1] >=
                                                   distance[i - 3] - distance[i - 5] and distance[i] >= distance[
                                                       i - 2] - distance[i - 4])) for i in
                                          range(3, len(distance)))


if __name__ == '__main__':
    s = Solution()

    print(s.isSelfCrossing([1, 2, 3, 4]))
