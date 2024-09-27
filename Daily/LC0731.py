from sortedcontainers import SortedDict

class MyCalendarTwo:
    def __init__(self):
        self.bookingCounts = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.bookingCounts[start] = self.bookingCounts.get(start, 0) + 1
        self.bookingCounts[end] = self.bookingCounts.get(end, 0) - 1
        runningSum = 0
        for count in self.bookingCounts.values():
            runningSum += count
            if runningSum > 2:
                self.bookingCounts[start] -= 1
                self.bookingCounts[end] += 1
                return False
        return True