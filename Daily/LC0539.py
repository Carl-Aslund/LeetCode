from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        minutes = sorted(int(time[:2])*60+int(time[3:]) for time in timePoints)
        minutes.append(minutes[0]+1440)
        minDiff = minutes[-1]
        for i in range(1, len(minutes)):
            minDiff = min(minDiff, minutes[i]-minutes[i-1])
        return minDiff
