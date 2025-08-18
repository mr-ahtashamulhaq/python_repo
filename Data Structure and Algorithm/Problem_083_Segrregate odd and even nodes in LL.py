"""Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity."""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def append_(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse_(self, node):
        current = node
        if current is None:
            print("LinkedList is Empty")
            return
        while current is not None:
            print(current.val, end="-->")
            current = current.next
        print("None")

    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_head = even

        while even is not None and even.next is not None:
            odd.next = odd.next.next        #type:ignore
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return head


if __name__ == "__main__":
    sol = Solution()
    sol.append_(1)
    sol.append_(2)
    sol.append_(3)
    sol.append_(4)
    sol.append_(5)

    new_head = sol.oddEvenList(sol.head)        #type:ignore

    print("Odd-Even Linked List:")
    sol.traverse_(new_head)
#Output : Odd-Even Linked List:
# 1-->3-->5-->2-->4-->None
