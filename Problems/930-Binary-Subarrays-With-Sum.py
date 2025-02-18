class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            if x < 0:
                return 0

            count = curr = st = 0
            for en in range(len(nums)):
                curr += nums[en]
                while curr > x:
                    curr -= nums[st]
                    st += 1
                
                count += (en - st + 1)
                
            return count

        return helper(goal) - helper(goal - 1)
