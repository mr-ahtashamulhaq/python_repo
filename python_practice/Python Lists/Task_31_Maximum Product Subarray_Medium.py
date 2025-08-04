"""Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[]."""
class Solution:
	def maxProduct(self,arr):
		maxprod = arr[0]
		minprod = arr[0]
		result = arr[0]
		
		for i in arr[1::]:
			if i < 0 :
				maxprod , minprod = minprod , maxprod
			maxprod = max(i , i * maxprod)
			minprod = min(i , i * minprod)
		result = max(result , maxprod)
		return result
	
obj = Solution()
arr = [-2, 6, -3, -10, 0, 2]
print(obj.maxProduct(arr))