class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for num in nums:
            if num & 1:
                odd.append(num)
            else:
                even.append(num)

        return even + odd
