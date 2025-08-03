"""You are given an array arr[] of non-negative integers. You have to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array."""
class Solution:
	def pushZerosToEnd(self,arr):
		for i in range(len(arr)):
			if arr[i] == 0:
				arr.append(arr.pop(i))
		return arr
	
obj = Solution()
arr  = [2,4,0,5,8,0,6,0]
print(obj.pushZerosToEnd(arr))