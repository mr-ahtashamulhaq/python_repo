"""You are given two linked lists representing two large positive numbers. The linked lists represent these two numbers, subtract the smaller number from the larger one and return the head of the linked list representing the result."""

class Solution:
    def subLinkedList(self, head1, head2):
        num1 = int(((str(head1).replace("[","")).replace("]","")).replace(", ",""))
        num2 = int(((str(head2).replace("[","")).replace("]","")).replace(", ",""))
        return num1-num2 if num1>num2 else num2-num1
        

obj = Solution()
l1 = [1,0,0]
l2 = [1,2]
print(obj.subLinkedList(l1,l2))