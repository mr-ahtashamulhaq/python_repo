"""Given an array of positive numbers, the task is to find the number of possible contiguous subarrays having product less than a given number k."""
#User function Template for python3

class Solution:
    def count_subarrays_brute_force(self,arr, k):
        count = 0
        n = len(arr)

        for i in range(n):
            product = 1
            for j in range(i, n):  
                product *= arr[j] 
                if product < k:
                    count += 1    
                else:
                    break
        return count

obj = Solution()
arr = [1, 2, 3, 4]
k = 10
print(obj.count_subarrays_brute_force(arr,k) )