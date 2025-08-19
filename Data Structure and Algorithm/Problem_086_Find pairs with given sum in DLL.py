"""Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target."""
from typing import Optional, List
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None


class Solution:
    def findPairsWithGivenSum(self, target: int, head: Optional['Node']) -> List[List[int]]:
        right = head
        result = []
        while right.next is not None:       #type:ignore
            right = right.next       #type:ignore
        left = head
        
        while (left is not None) and (right is not None) and left.data < right.data:
            total = left.data + right.data
            if total == target:
                result.append([left.data, right.data])
                right = right.prev
                left = left.next
            elif total < target:
                left = left.next
            else:
                right = right.prev
        return result


# Helper Functions 
def buildDLL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node       #type:ignore
        new_node.prev = current       #type:ignore
        current = new_node
    return head

def printDLL(head):
    res = []
    temp = head
    while temp:
        res.append(temp.data)
        temp = temp.next
    print("DLL:", " <-> ".join(map(str, res)))


arr = [1, 2, 3, 4, 5, 6, 7]
head = buildDLL(arr)

target = 8
sol = Solution()
pairs = sol.findPairsWithGivenSum(target, head)

print(f"Pairs with sum {target}: {pairs}")
# Output : Pairs with sum 8: [[1, 7], [2, 6], [3, 5]]