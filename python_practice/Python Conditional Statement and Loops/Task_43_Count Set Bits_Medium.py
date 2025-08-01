"""Given a positive integer n. Your task is to return the count of set bits."""
#User function Template for python3
class Solution:
	def setBits(self, n):
		binary = bin(n)
		setbits  = binary.count("1")
		return setbits

obj = Solution()
print(obj.setBits(3))