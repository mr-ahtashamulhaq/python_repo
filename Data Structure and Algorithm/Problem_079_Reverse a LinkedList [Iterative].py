"""Given the head of a singly linked list, reverse the list, and return the reversed list."""

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

    def reverseList(self, head: ListNode):
        temp = head
        prev = None

        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev


if __name__ == "__main__":
    sol = Solution()

    sol.append_(1)
    sol.append_(2)
    sol.append_(3)
    sol.append_(4)
    sol.append_(5)

    print("Original Linked List:", end="   ")
    sol.traverse_(sol.head)
    
    reversed_head = sol.reverseList(sol.head) #type: ignore

    print("Reversed Linked List:",end="   ")
    sol.traverse_(reversed_head)

# Output:

# Original Linked List:     1-->2-->3-->4-->5-->None
# Reversed Linked List:     5-->4-->3-->2-->1-->None