from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        patternLength, textLength = len(s1), len(s2)
        if patternLength > textLength:
            return False
        charCount = Counter()
        for patternChar, textChar in zip(s1, s2[:patternLength]):
            charCount[patternChar] -= 1
            charCount[textChar] += 1
        diffCount = sum(x != 0 for x in charCount.values())
        if diffCount == 0:
            return True
        for i in range(patternLength, textLength):
            charOut = s2[i - patternLength]
            charIn = s2[i]
            if charCount[charIn] == 0:
                diffCount += 1
            charCount[charIn] += 1
            if charCount[charIn] == 0:
                diffCount -= 1
            if charCount[charOut] == 0:
                diffCount += 1
            charCount[charOut] -= 1
            if charCount[charOut] == 0:
                diffCount -= 1
            if diffCount == 0:
                return True
        return False
