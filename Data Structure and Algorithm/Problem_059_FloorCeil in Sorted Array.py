"""Given a sorted array of integers nums (in ascending order) and an integer target, return an array of two elements:

The floor of target — the largest number in nums less than or equal to target.

The ceil of target — the smallest number in nums greater than or equal to target.

If the floor or ceil does not exist, represent it with -1."""
class Solution:
    def ceil_the_floor(self,nums,target):
        n= len(nums)
        floor = -1
        ceil = -1
        low = 0
        high = n-1

        while(low<=high):
            mid = (low+high)//2

            if nums[mid] == target:
                return [nums[mid] , nums[mid]]
            
            elif nums[mid] > target:
                ceil = nums[mid]
                high = mid -1
            else:
                floor = nums[mid]
                low = mid+1
        return [floor,ceil]
    
obj = Solution()
nums = [1,2,4,5,6,7,8]
target = 3
print(obj.ceil_the_floor(nums,target))
# Output : [2, 4]