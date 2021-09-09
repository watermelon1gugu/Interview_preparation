class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        res = 0
        i = 0
        while i < len(arr):
            res += arr[i] * (((i + 1) // 2) * ((len(arr) - i) // 2) + (i // 2 + 1) * ((len(arr) - i - 1) // 2 + 1))
            i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
