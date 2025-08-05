"""Given a string s which may contain lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be same as in the original string."""
class Solution:
	def removeDuplicates(self, s):
		seen = set(s)
		return "".join(seen)
		
obj = Solution()
print(obj.removeDuplicates("geEksforGEeks"))	