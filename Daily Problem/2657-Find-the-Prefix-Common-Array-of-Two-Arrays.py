class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        set_a = set()
        set_b = set()
        common = set()

        for i in range(len(A)):
            set_a.add(A[i])
            set_b.add(B[i])

            common.update(set_a & set_b)

            res.append(len(common))

        return res
