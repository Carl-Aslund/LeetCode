from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a > 0:
            heappush(maxHeap, [-a, 'a'])
        if b > 0:
            heappush(maxHeap, [-b, 'b'])
        if c > 0:
            heappush(maxHeap, [-c, 'c'])
        result = []
        while maxHeap:
            currentChar = heappop(maxHeap)
            if len(result) >= 2 and result[-1] == currentChar[1] and result[-2] == currentChar[1]:
                if not maxHeap:
                    break
                nextChar = heappop(maxHeap)
                result.append(nextChar[1])
                if -nextChar[0] > 1:
                    nextChar[0] += 1
                    heappush(maxHeap, nextChar)
                heappush(maxHeap, currentChar)
            else:
                result.append(currentChar[1])
                if -currentChar[0] > 1:
                    currentChar[0] += 1
                    heappush(maxHeap, currentChar)
        return ''.join(result)
