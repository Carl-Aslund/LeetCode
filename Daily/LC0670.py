class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        length = len(digits)
        maxDigitIndices = list(range(length))
        for i in range(length-2, -1, -1):
            if digits[i] <= digits[maxDigitIndices[i+1]]:
                maxDigitIndices[i] = maxDigitIndices[i+1]
        for i in range(length):
            maxIndex = maxDigitIndices[i]
            if digits[i] < digits[maxIndex]:
                digits[i], digits[maxIndex] = digits[maxIndex], digits[i]
                break
        return int(''.join(digits))
