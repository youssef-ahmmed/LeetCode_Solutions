class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        cur_max = cur_min = nums[0]
        prev_max = float("-inf")

        for num in nums:
            if num.bit_count() == cur_min.bit_count():
                cur_min = min(cur_min, num)
                cur_max = max(cur_max, num)
            else:
                if prev_max > cur_min:
                    return False
                prev_max = cur_max
                cur_max = cur_min = num

        return not (prev_max > cur_min)
