class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        sm = 0

        for i in range(k):
            hap = happiness[i] - i
            if hap > 0:
                sm += hap

        return sm