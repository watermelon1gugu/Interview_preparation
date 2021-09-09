class Solution:

    def numberOfArithmeticSlices(self, nums) -> int:
        if len(nums) < 3:
            return 0
        combo = 0
        res = 0
        temp_diff = nums[1] - nums[0]
        i = 1
        while i < len(nums):
            diff = nums[i] - nums[i - 1]
            if diff == temp_diff:
                combo += 1
                if combo >= 2:
                    res += combo - 1
            else:
                combo = 1
                temp_diff = diff
            i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfArithmeticSlices([1, 2, 3, 4, 5, 6]))
