class Solution:
    def longestCommonPrefix(self, arr):
        arr.sort()
        i = 0
        while i < len(arr[0]) and arr[0][i] == arr[-1][i]:
            i += 1
        return arr[0][:i]
    
obj = Solution()
li = ["geeksforgeeks", "geeks", "geek", "geezer"]
print(obj.longestCommonPrefix(li))