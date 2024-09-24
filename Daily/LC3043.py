from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for num in arr1:
            while num:
                prefixes.add(num)
                num //= 10
        maxPrefixLength = 0
        for num in arr2:
            while num:
                if num in prefixes:
                    maxPrefixLength = max(maxPrefixLength, len(str(num)))
                    break
                num //= 10
        return maxPrefixLength
