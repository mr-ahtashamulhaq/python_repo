"""Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.

Note: 'c' is the position of the node which is the next pointer of the last node of the linkedlist. If c is 0, then there is no loop."""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def append_(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node     #type: ignore

    def traverse_(self, node):
        current = node
        if current is None:
            print("LinkedList is Empty")
            return
        while current is not None:
            print(current.data, end="-->")
            current = current.next
        print("None")

    def lengthOfLoop(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = slow.next
                count = 1
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0


if __name__ == "__main__":

    sol1 = Solution()
    sol1.append_(1)
    sol1.append_(2)
    sol1.append_(3)
    sol1.append_(4)

    sol1.traverse_(sol1.head)
    print(sol1.lengthOfLoop(sol1.head))
     # Output: 0
