class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        def get_prime_before(num):
            for n in reversed(range(2, num)):
                if is_prime(n):
                    return n
            return 0

        def is_prime(num):
            if num <= 1:
                return False

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        prev = 0
        for num in nums:
            upper_bound = num - prev
            b_prime = get_prime_before(upper_bound)

            if num - b_prime <= prev:
                return False

            prev = num - b_prime

        return True