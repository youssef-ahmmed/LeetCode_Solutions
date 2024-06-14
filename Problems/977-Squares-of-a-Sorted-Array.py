class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1

        sorted_num = []
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                sorted_num.append(nums[j] ** 2)
                j -= 1
            else:
                sorted_num.append(nums[i] ** 2)
                i += 1

        return sorted_num[::-1]
