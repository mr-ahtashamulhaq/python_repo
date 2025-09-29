"""Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.
"""


class Solution:
    def recursion(self, i, arr, memo, k):
        # Base case: if pointer goes out of bounds, return 0
        if i >= len(arr):
            return 0

        # If result for this subproblem is already computed, return it
        if i in memo:
            return memo[i]

        current_max = 0
        result = 0

        # Iterate through possible subarray end points
        # The loop goes up to min(len(arr), i + k)
        # In Python, range is non-inclusive, so it's min(len(arr), i + k)
        for j in range(i, min(len(arr), i + k)):
            # Update the maximum element in the current window
            current_max = max(current_max, arr[j])

            # Calculate the size of the current window
            window_size = j - i + 1

            # Calculate the sum for the current partition
            # current_max * window_size gives the sum of the current subarray
            # dfs(j + 1) recursively solves the problem for the rest of the array
            current_sum = current_max * window_size + self.recursion(
                j + 1, arr, memo, k
            )

            result = max(result, current_sum)

        memo[i] = result
        return result

    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        memo = {}
        return self.recursion(0, arr, memo, k)


obj = Solution()
arr = [1, 15, 7, 9, 2, 5, 10]
k = 3
print(obj.maxSumAfterPartitioning(arr, k))

# Output : 84