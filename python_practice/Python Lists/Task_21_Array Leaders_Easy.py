"""You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader."""
class Solution:
    def leaders(self, arr):
        i = 0
        while(i-1 < len(arr)):


            for j in range(i+1,len(arr)):

                if arr[i]<arr[j]:
                    arr.pop(i)
                    i -= 1
                    break
            
            i+=1
        return arr
obj = Solution()
arr = [10, 4, 2, 4, 1]
print(obj.leaders(arr))