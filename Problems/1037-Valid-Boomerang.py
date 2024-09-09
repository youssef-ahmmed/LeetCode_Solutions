class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        point1, point2, point3 = points

        x1, y1 = point1
        x2, y2 = point2
        x3, y3 = point3

        area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

        return area > 0
