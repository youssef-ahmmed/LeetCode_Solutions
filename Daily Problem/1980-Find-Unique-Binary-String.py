class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        bin_nums = set(nums)

        for i in range(2 ** n):
            bin_num = bin(i)[2:].zfill(n)
            if bin_num not in bin_nums:
                return bin_num
