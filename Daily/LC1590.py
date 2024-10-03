from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p
        if remainder == 0:
            return 0
        modIndices = {0: -1}
        currentMod = 0
        minLength = len(nums)
        for i, num in enumerate(nums):
            currentMod = (currentMod + num) % p
            targetMod = (currentMod - remainder + p) % p
            if targetMod in modIndices:
                minLength = min(minLength, i - modIndices[targetMod])
            modIndices[currentMod] = i
        return -1 if minLength == len(nums) else minLength
