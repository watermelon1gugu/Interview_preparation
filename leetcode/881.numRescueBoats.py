class Solution:
    def numRescueBoats(self, people: list, limit: int) -> int:
        people.sort()
        res = 0
        light, heavy = 0, len(people) - 1
        while light <= heavy:
            if people[light] + people[heavy] <= limit:
                light += 1
            res += 1
            heavy -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numRescueBoats([1, 2], 2))
