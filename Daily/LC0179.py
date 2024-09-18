from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        nums.sort(key=cmp_to_key(self.compareNumbers))
        if nums[0] == "0":
            return "0"
        return ''.join(nums)

    def compareNumbers(self, a: str, b: str) -> int:
        if a + b < b + a:
            return 1
        else:
            return -1
