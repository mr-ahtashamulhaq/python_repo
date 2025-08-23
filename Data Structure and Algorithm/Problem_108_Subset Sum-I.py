"""Given a array arr of integers, return the sums of all subsets in the list.  Return the sums in any order."""
class Solution:
	def solve(self,ind,total,result,arr):
		if ind >= len(arr):
			result.append(total)
			return
			
		sum = total + arr[ind]
		self.solve(ind+1, sum,result,arr)
		sum = total
		self.solve(ind+1, sum,result,arr)
		
		
	def subsetSums(self, arr):
		# code here
		result = []
		self.solve(0,0,result,arr)
		return result
		
obj = Solution()
print(obj.subsetSums([2,3,5]))
# Output : [10, 5, 7, 2, 8, 3, 5, 0]