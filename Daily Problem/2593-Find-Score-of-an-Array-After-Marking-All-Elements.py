class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        sorted_num = [(num, idx) for idx, num in enumerate(nums)]
        sorted_num.sort()
        marked = [False] * len(nums)

        for i in range(len(nums)):
            num = sorted_num[i][0]
            idx = sorted_num[i][1]

            if not marked[idx]:
                score += num
                marked[idx] = True

                if idx - 1 >= 0:
                    marked[idx - 1] = True
                if idx + 1 < len(nums):
                    marked[idx + 1] = True

        return score        
