class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        set_a = set()
        set_b = set()
        
        for i in range(n):
            res[i] = res[i - 1]
            if A[i] == B[i]:
                res[i] += 1
            else:
                if A[i] in set_b:
                    res[i] += 1
                if B[i] in set_a:
                    res[i] += 1
                set_a.add(A[i])
                set_b.add(B[i])
            
        return res
