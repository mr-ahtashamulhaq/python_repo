"""You are given an array of k linked-lists lists, 
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
import heapq
from typing import List, Optional


# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[Node]]) -> Optional[Node]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = Node()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = node

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# ------------ Helper Functions ------------

def build_linked_list(arr: List[int]) -> Optional[Node]:
    """Convert Python list to linked list."""
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head


def linked_list_to_list(head: Optional[Node]) -> List[int]:
    """Convert linked list to Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result



if __name__ == "__main__":
    list1 = build_linked_list([1, 4, 5])
    list2 = build_linked_list([1, 3, 4])
    list3 = build_linked_list([2, 6])

    lists = [list1, list2, list3]

    solution = Solution()
    merged_head = solution.mergeKLists(lists)

    print("Merged Linked List:", linked_list_to_list(merged_head))

# Output : Merged Linked List: [1, 1, 2, 3, 4, 4, 5, 6]