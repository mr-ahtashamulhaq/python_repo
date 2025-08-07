"""Given an array nums of n elements and q queries . Each query consists of two integers l and r . You task is to find the number of elements of nums[] in range [l,r] which occur atleast k times."""
class Solution:
    def processQueries(self, nums, queries, k):

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        results = []

        for l, r in queries:
            seen = set()
            count = 0
            for i in range(l, r + 1):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    if freq[nums[i]] >= k:
                        count += 1
            results.append(count)

        return results


nums = [1, 2, 2, 3, 3, 3, 4]
queries = [(0, 6), (1, 4), (2, 5)]
k = 2

sol = Solution()
answers = sol.processQueries(nums, queries, k)
for ans in answers:
    print(ans)