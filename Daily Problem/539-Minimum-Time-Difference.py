class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def calc_minutes(period):
            time = period.split(':')
            hours, minutes = int(time[0]), int(time[1])

            return hours * 60 + minutes

        minutes = list(map(calc_minutes, timePoints))
        minutes.sort()

        mindiff = float('inf')

        for i in range(len(minutes) - 1):
            diff = abs(minutes[i] - minutes[i + 1])
            mindiff = min(mindiff, diff, 60 * 24 - diff)

        mindiff = min(
            mindiff,
            abs(minutes[0] - minutes[-1]),
            60 * 24 - abs(minutes[0] - minutes[-1]))

        return mindiff
