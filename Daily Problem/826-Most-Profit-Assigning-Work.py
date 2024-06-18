class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        total_profit = 0
        max_profit = 0
        idx = 0

        for a in worker:
            while idx < len(jobs) and a >= jobs[idx][0]:
                max_profit = max(max_profit, jobs[idx][1])
                idx += 1

            total_profit += max_profit

        return total_profit
