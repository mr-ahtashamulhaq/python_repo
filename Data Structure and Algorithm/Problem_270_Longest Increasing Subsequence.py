"""Given an array arr[] of non-negative integers, the task is to find the length of the Longest Strictly Increasing Subsequence (LIS).

A subsequence is strictly increasing if each element in the subsequence is strictly less than the next element."""
class Solution:
    # Simple binary search function to find first position  where tails[pos] is greater or equal to x
    def find_position(self, x, arr):
        low = 0
        high = len(arr) - 1

        ans = len(arr)
        while low <= high:
            mid = (high + low) // 2

            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def lis(self, arr):
        n = len(arr)
        if n == 0:
            return []

        temp = []  # stores the temporary LIS values
        for x in arr:
            pos = self.find_position(x, temp)

            if pos == len(temp):
                # x is greater than all tails, so extend
                temp.append(x)

            else:
                # replace to maintain best tail
                temp[pos] = x

        # length of tails = length of LIS
        return len(temp)


obj = Solution()
arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(obj.lis(arr))

# Output : 4