"""You are given the head_ref of a doubly Linked List and a Key. Your task is to delete all occurrences of the given key if it is present and return the new DLL."""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def deleteAllOccurOfX(self, head, x):
        if head.next is None and head.data == x:
            return None
            
        temp = head
        previous = None
        new_head = head
        
        while temp is not None:
            if temp.data == x:
                
                if previous is not None:
                    previous.next = temp.next
                
                if temp.next is not None:
                    temp.next.prev = previous
                
                if temp == new_head:
                    new_head = new_head.next
            else:
                previous = temp #Move previous only if node is NOT deleted
            temp = temp.next
        return new_head


#to Build DLL
def buildDLL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node     #type: ignore
        new_node.prev = current     #type: ignore
        current = new_node
    return head

#To Traverse
def printDLL(head):
    res = []
    temp = head
    while temp:
        res.append(temp.data)
        temp = temp.next
    print("DLL:", " <-> ".join(map(str, res)))


arr = [2, 3, 2, 4, 2, 5]
head = buildDLL(arr)
x = 2
sol = Solution()
head = sol.deleteAllOccurOfX(head, x)

print(f"After deleting {x}:")
printDLL(head)

# After deleting 2:
# DLL: 3 <-> 4 <-> 5