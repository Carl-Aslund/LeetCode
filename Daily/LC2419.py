from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxValue = max(nums)
        longestLength = currentLength = 0
        for n in nums:
            if n == maxValue:
                currentLength += 1
                longestLength = max(longestLength, currentLength)
            else:
                currentLength = 0
        return longestLength
