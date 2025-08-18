"""Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list."""
# Definition for singly-linked list.
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

    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next     #type: ignore
            fast = fast.next.next

            if fast == slow:
                slow = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next     #type: ignore
                return slow     #type: ignore
        return None     #type: ignore


if __name__ == "__main__":
    sol1 = Solution()
    sol1.append_(1)
    sol1.append_(2)
    sol1.append_(3)
    sol1.append_(4)
    
    sol1.traverse_(sol1.head)
    cycle_node = sol1.detectCycle(sol1.head)     #type: ignore
    print( cycle_node)  
    # Output:  None