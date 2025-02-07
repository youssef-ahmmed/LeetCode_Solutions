class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colored_balls = {}
        distinct_colors = defaultdict(set)
        res = []

        for ball, color in queries:
            if ball in colored_balls:
                distinct_colors[colored_balls[ball]].discard(ball)
                if len(distinct_colors[colored_balls[ball]]) == 0:
                    del distinct_colors[colored_balls[ball]]

            colored_balls[ball] = color
            distinct_colors[color].add(ball)
            res.append(len(distinct_colors))

        return res
