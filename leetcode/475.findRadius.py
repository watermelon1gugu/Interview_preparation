class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()
        houses.sort()
        r = 0
        i = 0
        heaters = [float("-inf")] + heaters + [float("inf")]
        for house in houses:
            while house > heaters[i]:
                i += 1
            r = max(r, min(heaters[i] - house, house - heaters[i - 1]))
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.findRadius([282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923],
                       [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729, 823378840,
                        143542612]))
