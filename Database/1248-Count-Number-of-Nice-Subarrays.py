class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def is_odd(num):
            return num % 2 != 0
    
        count = 0
        
        prefix_count = {0: 1}
        
        odd_count = 0
        
        for num in nums:
            if is_odd(num):
                odd_count += 1
            
            if odd_count - k in prefix_count:
                count += prefix_count[odd_count - k]
            
            if odd_count in prefix_count:
                prefix_count[odd_count] += 1
            else:
                prefix_count[odd_count] = 1
        
        return count
