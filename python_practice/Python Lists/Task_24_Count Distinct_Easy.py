"""You are given a list arr that contains integers. You need to count distinct integers in list."""

class Solution:
    def countDistinct(self, arr):
        distinct = []

        for i in range(len(arr)):
            if arr[i] not in distinct:
                distinct.append(arr[i])

        return len(distinct)

obj = Solution()
arr = [4, 4, 5, 4, 3, 8, 4, 2, 4, 8, 1, 7]
print(obj.countDistinct(arr))