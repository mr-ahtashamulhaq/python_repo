"""Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false."""

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

    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next        #type:ignore
            fast = fast.next.next

            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    # Test 1: Linked List without cycle
    sol1 = Solution()
    sol1.append_(1)
    sol1.append_(2)
    sol1.append_(3)
    sol1.append_(4)

    sol1.traverse_(sol1.head)
    print( sol1.hasCycle(sol1.head))        #type:ignore
# Output :  False
