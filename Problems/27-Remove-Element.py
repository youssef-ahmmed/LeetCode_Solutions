class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)

        while count:
            nums.remove(val)
            count -= 1
        return len(nums)
