class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums)

        return nums

    def merge_sort(self, nums: List[int]) -> None:
        if len(nums) > 1:
            mid = len(nums) // 2

            left_half = nums[:mid]
            right_half = nums[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            self.merge(nums, left_half, right_half)

    def merge(self, nums: List[int], left_half: List[int], right_half: List[int]) -> None:
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                nums[k] = right_half[j]
                j += 1
            else:
                nums[k] = left_half[i]
                i += 1
            k += 1

        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1
