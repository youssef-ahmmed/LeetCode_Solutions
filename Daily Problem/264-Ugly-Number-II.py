class Solution:
    def nthUglyNumber(self, n: int) -> int:
        memory = {1}
        heap = [1]
        ugly = None

        for _ in range(n):
            ugly = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                new_ugly = ugly * factor
                if new_ugly not in memory:
                    memory.add(new_ugly)
                    heapq.heappush(heap, new_ugly)

        return ugly
