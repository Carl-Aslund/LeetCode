class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return length
        chars = set()
        l = r = 0
        result = 0
        while r < length:
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            r += 1
            result = max(result, r-l)
        return result