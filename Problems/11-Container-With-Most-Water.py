class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1

        max_area = 0
        while i < j:
            max_area = max(min(height[i], height[j]) * (j - i), max_area)

            if height[i] >= height[j]:
                j -= 1
            elif height[i] < height[j]:
                i += 1
    
        return max_area
