class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float('-inf')

        for num in nums:
            if num > max1:
                max3, max2, max1 = max2, max1, num
            elif max1 > num > max2:
                max3, max2 = max2, num
            elif max2 > num > max3:
                max3 = num

        return max1 if max3 == float('-inf') else max3
