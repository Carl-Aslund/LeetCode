from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = Counter(s)
        for char in t:
            s_counter[char] -= 1
            if s_counter[char] < 0:
                return False
        return True
