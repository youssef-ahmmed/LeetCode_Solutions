class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        st = 0
        picked = defaultdict(int)

        for en in range(len(fruits)):
            picked[fruits[en]] += 1

            while len(picked) > 2:
                picked[fruits[st]] -= 1
                if picked[fruits[st]] == 0:
                    del picked[fruits[st]]
                st += 1
            res = max(res, en - st + 1)

        return res
