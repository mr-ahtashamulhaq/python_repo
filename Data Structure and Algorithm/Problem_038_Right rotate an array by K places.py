"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative."""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(nums,l,r):
            while(l<r):
                nums[l] , nums[r] = nums[r] , nums[l]
                r -=1
                l+=1
        n = len(nums)
        #To check  exact number of rotaions (incase if k > n)
        k = k%n
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-k-1)
        reverse(nums,0,n-1)
obj = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
obj.rotate(nums,k)
print(nums)
# Output: [5,6,7,1,2,3,4]