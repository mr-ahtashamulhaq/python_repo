"""Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.
Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays."""

class Solution:
    def findUnion(self, a, b):
        # code here 
        n = len(a)
        m = len(b)
        i , j = 0 , 0
        result  = []

        while(i<n and j<m):
            if (a[i] <= b[j]):
                if len(result) == 0 or result[-1] != a[i]:
                    result.append(a[i])
                i+=1
            else:
                if len(result) == 0 or result[-1] != b[j]:
                    result.append(b[j])
                j+=1

        while i < n: 
            if len(result) == 0 or result[-1] != a[i]:
                result.append(a[i])
            i += 1

        while j < m:
            if len(result) == 0 or result[-1] != b[j]: 
                result.append(b[j])
            j += 1
        return result
obj = Solution()
a = [1,1,1,2,4,6,7]
b = [1, 2, 3, 6, 7, 8, 9, 10]
print(obj.findUnion(a,b))

# Output : [1, 2, 3, 4, 6, 7, 8, 9, 10]