"""Given an integer i. Print the maximum number of nodes on level i of a binary tree.

Note: The level of a binary tree starts with 1 (i.e., level 1 contains the root of the tree, level 2 contains the children of the root, and so on)."""
class Solution:
    def countNodes(self, i):
        # Code here
        return 2**(i-1)
    
obj = Solution()
print(obj.countNodes(3))
# Output : 4