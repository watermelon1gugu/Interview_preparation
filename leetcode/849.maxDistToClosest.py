class Solution:
    def maxDistToClosest(self, seats) -> int:
        max_combo = 0
        combo = 0
        head_combo = -1
        for seat in seats:
            if seat == 1:
                max_combo = max(combo, max_combo)
                if head_combo == -1:
                    head_combo = combo
                combo = 0
            else:
                combo += 1
        tail_combo = combo

        return max(head_combo, int((max_combo + 1) / 2), tail_combo)


if __name__ == '__main__':
    s = Solution()
    print(s.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
