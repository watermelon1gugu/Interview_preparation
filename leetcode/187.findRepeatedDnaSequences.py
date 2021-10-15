class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if len(s) <= 10:
            return []
        book = set()
        res = set()
        for i in range(9, len(s)):
            if s[i - 9: i+1] not in book:
                book.add(s[i - 9: i+1])
            else:
                res.add(s[i - 9: i+1])
        return list(res)

if __name__ == '__main__':
    s = Solution()
    print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))