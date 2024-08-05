class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        kth = 0
        
        for a in arr:
            if freq[a] == 1:
                kth += 1
            if kth == k:
                return a
            
        return ""
