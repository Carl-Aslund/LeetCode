from sortedcontainers import SortedDict

class MyCalendar:
    def __init__(self):
        self.sortedEvents = SortedDict()

    def book(self, start: int, end: int) -> bool:
        nextEventIndex = self.sortedEvents.bisect_right(start)
        if nextEventIndex < len(self.sortedEvents) and end > self.sortedEvents.values()[nextEventIndex]:
            return False
        self.sortedEvents[end] = start
        return True