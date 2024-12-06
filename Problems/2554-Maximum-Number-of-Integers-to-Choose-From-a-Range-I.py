class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        nums = []
        banned_set = set(banned)

        for i in range(1, n + 1):
            if i not in banned_set:
                nums.append(i)

        total_sum = 0
        count = 0

        for num in nums:
            if total_sum + num <= maxSum:
                total_sum += num
                count += 1
            else:
                break

        return count
