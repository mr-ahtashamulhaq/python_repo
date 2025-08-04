"""Given an array, arr[], determine if arr can be split into three consecutive parts such that the sum of each part is equal. If possible, return any index pair(i, j) in an array such that sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1]), otherwise return an array {-1,-1}.

Note: Since multiple answers are possible, return any of them. The driver code will print true if it is correct otherwise, it will print false."""
class Solution:
    def split_array_into_three_equal_parts(self,arr):
        n = len(arr)

        for i in range(n - 2):
            sum1 = sum(arr[0:i+1])

            for j in range(i + 1, n - 1):
                sum2 = sum(arr[i+1:j+1])
                sum3 = sum(arr[j+1:])

                if sum1 == sum2 == sum3:
                    return [i, j]

        return [-1, -1]


obj = Solution()
arr = [1, 3, 4, 0, 4]
print( obj.split_array_into_three_equal_parts(arr))