class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countPrefix(prefix):
            nextPrefix = prefix + 1
            total = 0
            while prefix <= n:
                total += min(n - prefix + 1, nextPrefix - prefix)
                nextPrefix *= 10
                prefix *= 10
            return total
        current = 1
        k -= 1
        while k:
            count = countPrefix(current)
            if k >= count:
                k -= count
                current += 1
            else:
                k -= 1
                current *= 10
        return current
