from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None
        midpoint = len(nums)//2
        return TreeNode(nums[midpoint], self.sortedArrayToBST(nums[:midpoint]), self.sortedArrayToBST(nums[midpoint+1:]))