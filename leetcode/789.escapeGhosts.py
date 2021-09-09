class Solution:
    def get_dis(self, target, now):
        dis = 0
        for i in range(2):
            dis += target[i] - now[i] if target[i] > now[i] else now[i] - target[i]

        return dis

    def escapeGhosts(self, ghosts, target) -> bool:
        i_dis = self.get_dis(target, [0, 0])
        for ghost in ghosts:
            if self.get_dis(target, ghost) <= i_dis:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.escapeGhosts([[5,0],[-10,-2],[0,-5],[-2,-2],[-7,1]], [7,7]))
