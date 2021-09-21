class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0:
            if s[i] == " ":
                i -= 1
                continue
            break
        k = i
        while k >= 0:
            if s[k] == " ":
                break
            k -= 1
        return i - k


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("   fly me   to   the moon  "))
