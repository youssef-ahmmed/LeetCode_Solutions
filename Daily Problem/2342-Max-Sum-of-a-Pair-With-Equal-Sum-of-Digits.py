class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(int)
        max_sum = -1

        def sum_digits(num: int):
            s = 0
            while num:
                d = num % 10
                num //= 10
                s += d
            return s

        for n in nums:
            dig_sum = sum_digits(n)

            if dig_sum in d:
                max_sum = max(max_sum, n + d[dig_sum])
            
            d[dig_sum] = max(d[dig_sum], n)

        return max_sum
