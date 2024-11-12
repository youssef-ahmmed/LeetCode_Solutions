class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = sorted([(q, i) for i, q in enumerate(queries)])

        n = len(queries)
        res = [0] * n

        max_beauty = 0
        cur_idx = 0

        for q, i in queries:
            while cur_idx < len(items) and items[cur_idx][0] <= q:
                max_beauty = max(max_beauty, items[cur_idx][1])
                cur_idx += 1

            res[i] = max_beauty

        return res
