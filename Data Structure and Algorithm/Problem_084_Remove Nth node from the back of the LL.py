"""Given the head of a linked list, remove the nth node from the end of the list and return its head"""
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

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next        #type:ignore
        if fast is None:
            return head.next        #type:ignore

        while fast.next is not None:
            slow = slow.next        #type:ignore
            fast = fast.next
        slow.next = slow.next.next        #type:ignore
        return head


if __name__ == "__main__":
    sol = Solution()
    sol.append_(1)
    sol.append_(2)
    sol.append_(3)
    sol.append_(4)
    sol.append_(5)

    new_head = sol.removeNthFromEnd(sol.head, 2)        #type:ignore

    sol.traverse_(new_head)
    #Output : 1-->2-->3-->5-->None
