from functools import lru_cache
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(maxsize=None)
        def computeAllWays(subExpr: str) -> List[int]:
            if subExpr.isdigit():
                return [int(subExpr)]
            results = []
            for i, char in enumerate(subExpr):
                if char in '+-*':
                    leftResults = computeAllWays(subExpr[:i])
                    rightResults = computeAllWays(subExpr[i+1:])
                    for leftVal in leftResults:
                        for rightVal in rightResults:
                            if char == '+':
                                results.append(leftVal+rightVal)
                            elif char == '-':
                                results.append(leftVal-rightVal)
                            else:
                                results.append(leftVal*rightVal)
            return results
        return computeAllWays(expression)
