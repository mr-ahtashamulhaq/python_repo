"""You are given an array arr[] of integer. You have to construct the singly linked list from the elements of arr[] and return the head of the linked list."""
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

    #to append new values/data
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current =   current.next
            current.next = new_node     #type: ignore

    #main method
    def constructLL(self, arr):
        for i in arr:
            self.append(i)
        return self.head

sll1 = Solution()
arr= [1,2,3,4,5]
sll1.constructLL(arr)
print(sll1.head.data)       #type: ignore
# output : 1