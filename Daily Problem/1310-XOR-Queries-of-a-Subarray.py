class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        pre = [arr[0]]

        for i in range(1, len(arr)):
            pre.append(arr[i] ^ pre[i - 1])

        for i in range(len(queries)):
            left, right = queries[i][0], queries[i][1]
            val = pre[right] if left == 0 else pre[right] ^ pre[left - 1]
            ans.append(val)
        
        return ans
