"""Python program to find the length of the longest
subarray having sum k using nested loop

Function to find longest sub-array having sum k"""
def longestSubarray(arr, k):
    res = 0
    for i in range(len(arr)):
        
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
          
            if sum == k:
              
                subLen = j - i + 1
                res = max(res, subLen)
    
    return res

arr = [10, 5, 2, 7, 1, -10] 
k = 15
print(longestSubarray(arr, k))