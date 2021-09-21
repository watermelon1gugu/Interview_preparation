class Solution:
    def findLongestWord(self, s: str, dictionary) -> str:
        m = {}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = [i]
            else:
                m[s[i]].append(i)
        res = ""
        for d in dictionary:
            temp_index = -1
            flag = True
            for c in d:
                if c not in m or max(m[c]) <= temp_index:
                    flag = False
                    break
                for i in m[c]:
                    if i > temp_index:
                        temp_index = i
                        break
            if flag:
                if len(res) < len(d):
                    res = d
                elif len(res) == len(d) and res > d:
                    res = d

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findLongestWord(s="abpcplea", dictionary=["ale", "apple", "monkey", "plea"]))
    print("abe" < "abc")
