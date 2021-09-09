class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0
        m_a = {}
        m_b = {}
        m_c = {}
        for char in secret:
            if char not in m_b:
                m_b[char] = 1
            else:
                m_b[char] += 1
        for char in guess:
            if char not in m_c:
                m_c[char] = 1
            else:
                m_c[char] += 1
        for i in range(len(guess)):
            if i == len(secret):
                break
            if secret[i] == guess[i]:
                a += 1
                m_b[secret[i]] -= 1
                m_c[secret[i]] -= 1
                if secret[i] not in m_a:
                    m_a[secret[i]] = 1
                else:
                    m_a[secret[i]] += 1
        for k, v in m_c.items():
            if k not in m_b:
                continue
            b += min(m_b[k], m_c[k])
        return f"{a}A{b}B"


if __name__ == '__main__':
    s = Solution()
    print(s.getHint("1123","0111"))
