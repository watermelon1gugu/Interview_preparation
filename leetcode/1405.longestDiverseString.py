class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = ""
        l = [{"n": a, "c": "a"}, {"n": b, "c": "b"}, {"n": c, "c": "c"}]
        l.sort(key=lambda x: x["n"], reverse=True)
        while l[0]["n"] > 0 or l[1]["n"] > 0 or l[2]["n"] > 0:
            flag = True
            for i in range(3):
                if len(s) < 2 or ((l[i]["c"] != s[-1] or s[-1] != s[-2]) and l[i]["n"] > 0):
                    s += l[i]["c"]
                    l[i]["n"] -= 1
                    l.sort(key=lambda x: x["n"], reverse=True)
                    flag = False
                    break
            if flag:
                break
        return s


if __name__ == '__main__':
    print(Solution().longestDiverseString(a=1, b=1, c=7))
