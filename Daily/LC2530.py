from heapq import heapify, heappop, heappush
from math import ceil
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        minHeap = [-num for num in nums]
        heapify(minHeap)
        total = 0
        for _ in range(k):
            val = -heappop(minHeap)
            total += val
            newVal = -(ceil(val/3))
            heappush(minHeap, newVal)
        return total
