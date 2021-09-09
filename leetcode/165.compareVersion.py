class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        n = max(len(version1), len(version2))
        for _ in range(n - len(version1)):
            version1.append("0")
        for _ in range(n - len(version2)):
            version2.append("0")
        for i in range(n):
            v1 = int(version1[i])
            v2 = int(version2[i])
            if v1 == v2:
                continue
            elif v1 > v2:
                return 1
            else:
                return -1
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.compareVersion("7.5.2.4", "7.5.3"))
