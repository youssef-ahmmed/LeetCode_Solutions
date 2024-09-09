class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calc_distance(point):
            return point[0] ** 2 + point[1] ** 2

        distance = []

        for point in points:
            heapq.heappush(distance, (calc_distance(point), point))
        
        small_dist = []

        for _ in range(k):
            dist, point = heapq.heappop(distance)
            small_dist.append(point)

        return small_dist
