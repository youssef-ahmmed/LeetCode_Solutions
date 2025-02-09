class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good = 0
        total = 0
        count = defaultdict(int)

        for i in range(len(nums)):
            total += i
            good += count[nums[i] - i]
            count[nums[i] - i] += 1

        return total - good
