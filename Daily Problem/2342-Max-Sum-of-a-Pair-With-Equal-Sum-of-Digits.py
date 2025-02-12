class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(list)

        def sum_digits(num: int):
            s = 0
            while num:
                d = num % 10
                num //= 10
                s += d
            return s
        
        for n in nums:
            heapq.heappush(d[sum_digits(n)], -n)

        max_sum = 0
        for heap in d.values():
            if len(heap) > 1:
                num1, num2 = -heapq.heappop(heap), -heapq.heappop(heap)
                max_sum = max(max_sum, num1 + num2)

        return max_sum if max_sum else -1
