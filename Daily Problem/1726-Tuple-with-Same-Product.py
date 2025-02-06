class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod = defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                prod[nums[i] * nums[j]] += 1

        count = 0
        for val in prod.values():
            count += 4 * val * (val - 1)

        return count
