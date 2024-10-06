class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1, words2 = sentence1.split(), sentence2.split()
        len1, len2 = len(words1), len(words2)
        if len1 < len2:
            words1, words2 = words2, words1
            len2, len1 = len1, len2
        start = end = 0
        while start < len2 and words1[start] == words2[start]:
            start += 1
        while end < len2 and words1[len1-1 - end] == words2[len2-1 - end]:
            end += 1
        return start + end >= len2
