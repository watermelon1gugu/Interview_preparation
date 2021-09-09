class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        f = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        f[0][0] = True
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                p = i + j - 1
                if i > 0:
                    f[i][j] = f[i][j] or (f[i - 1][j] and s1[i-1] == s3[p])
                if j > 0:
                    f[i][j] = f[i][j] or (f[i][j - 1] and s2[j-1] == s3[p])
        return f[len(s1)][len(s2)]


if __name__ == '__main__':
    s = Solution()
    print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
