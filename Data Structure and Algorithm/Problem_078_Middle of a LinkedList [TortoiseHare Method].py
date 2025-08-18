"""Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node."""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def __init__(self):
		self.head = None
		
		
	def append(self,val):
		new_node = ListNode(val)
		temp = self.head
		if temp is None:
			self.head = new_node
		else:
			while temp.next is not None:
				temp = temp.next
			temp.next = new_node
			
	def middleNode(self):
		slow = self.head
		fast = self.head
		while fast is not None and fast.next is not None:
			fast = fast.next.next
			slow = slow.next      #type: ignore
		return slow

sll1 = Solution()
values = [1,2,3,4,5]
for i in values:
    sll1.append(i)
mid= sll1.middleNode()
print(mid.val)      #type: ignore

# output: 3

