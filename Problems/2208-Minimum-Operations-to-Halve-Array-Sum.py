class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        half = total / 2
        min_oper = 0

        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        while total > half:
            num_half = -heapq.heappop(max_heap) / 2
            heapq.heappush(max_heap, -num_half)
            total -= num_half
            min_oper += 1

        return min_oper
