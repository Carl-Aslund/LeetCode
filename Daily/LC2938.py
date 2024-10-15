class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        answer, oneCount = 0, 0
        for i in reversed(range(n)):
            if s[i] == '1':
                oneCount += 1
                answer += (n - i - 1) - oneCount + 1
        return answer
