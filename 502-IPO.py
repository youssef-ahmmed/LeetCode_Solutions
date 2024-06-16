class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(c, p) for c, p in zip(capital, profits)]
        projects = sorted(projects, key=lambda x: x[0])

        total_capital = w

        heap = []
        heapify(heap)

        idx = 0
        for i in range(k):
            while idx < len(projects) and total_capital >= projects[idx][0]:
                heappush(heap, -projects[idx][1])
                idx += 1

            if not heap:
                break

            total_capital += -heappop(heap)

        return total_capital
