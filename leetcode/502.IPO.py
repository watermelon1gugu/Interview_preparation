import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        if w > max(capital):
            return w + sum(heapq.nlargest(k, profits))
        arr = [(capital[i], profits[i]) for i in range(len(profits))]
        arr.sort(key=lambda x: x[0])

        pq = []
        curr = 0
        for _ in range(k):
            while curr < len(arr) and w >= arr[curr][0]:
                heapq.heappush(pq, -arr[curr][1])
                curr += 1
            if pq:
                w -= heapq.heappop(pq)
            else:
                break
        return w


if __name__ == '__main__':
    s = Solution()
    print(s.findMaximizedCapital(k=10, w=0, profits=[1, 2, 3], capital=[0, 1, 2]))
