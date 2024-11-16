class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(len(nums) - k + 1):
            flag = False
            for j in range(i, i + k - 1):
                if nums[j + 1] - nums[j] != 1:
                    res.append(-1)
                    flag = True
                    break
            if not flag:
                res.append(nums[i + k - 1])
                
        return res
