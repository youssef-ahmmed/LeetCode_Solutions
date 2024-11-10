class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        bits = [0] * 32
        min_len = float("inf")

        def update_bits(bits, n, diff):
            for i in range(32):
                if n & (1 << i):
                    bits[i] += diff

        def convert_bits_to_num(bits):
            num = 0
            for i in range(32):
                if bits[i]:
                    num += (1 << i)

            return num

        for r in range(len(nums)):
            update_bits(bits, nums[r], 1)
            cur_or = convert_bits_to_num(bits)

            while l <= r and cur_or >= k:
                min_len = min(min_len, r - l + 1)
                update_bits(bits, nums[l], -1)
                cur_or = convert_bits_to_num(bits)

                l += 1

        return -1 if min_len == float("inf") else min_len
