"""Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the linked list"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def removeDuplicates(self, head):
        current = head
        while current is not None:
            if current.prev is not None and current.data == current.prev.data:
                if current.prev == head:
                    current.prev = None
                    head = current
                else:
                    current.prev.prev.next = current
                    current.prev = current.prev.prev
            current = current.next
        return head

#Helper Functions 
def build_doubly_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        new_node = Node(val)
        current.next = new_node     #type:ignore
        new_node.prev = current     #type:ignore
        current = new_node
    return head

def print_doubly_linked_list(head):
    """Prints the doubly linked list."""
    values = []
    current = head
    while current:
        values.append(current.data)
        current = current.next
    print(" -> ".join(map(str, values)))

if __name__ == "__main__":
    values = [1, 1, 2, 3, 3, 4, 5, 5]
    head = build_doubly_linked_list(values)

    print("After Removing Duplicates:")
    sol = Solution()
    new_head = sol.removeDuplicates(head)
    print_doubly_linked_list(new_head)
# Output: 
# After Removing Duplicates:
# 1 -> 2 -> 3 -> 4 -> 5