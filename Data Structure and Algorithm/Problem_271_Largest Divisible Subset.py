"""Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them."""
class Solution:
    # USING MEMOIZAITON
    def recursion(self, i, nums, cache):
        if i == len(nums):
            return []

        if i in cache:
            return cache[i]

        res = []
        res.append(nums[i])

        for j in range(i + 1, len(nums)):

            if nums[j] % nums[i] == 0:

                pick = [nums[i]] + self.recursion(j, nums, cache)
                if len(res) < len(pick):
                    res = pick

        cache[i] = res
        return cache[i]

    def largestDivisibleSubset(self, nums):
        nums.sort()
        cache = {}
        result = []

        for i in range(len(nums)):
            temp = self.recursion(i, nums, cache)
            if len(temp) > len(result):
                result = temp

        return result


obj = Solution()
nums = [1, 2, 4, 8, 32, 16]
print(obj.largestDivisibleSubset(nums))

# Output : [1, 2, 4, 8, 16, 32]