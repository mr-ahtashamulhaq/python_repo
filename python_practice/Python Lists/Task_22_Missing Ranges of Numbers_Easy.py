"""You have an inclusive interval [lower, upper] and a sorted array of unique integers arr[], all of which lie within this interval. A number x is considered missing if x is in the range [lower, upper] but not present in arr[]. Your task is to return the smallest set of sorted ranges that includes all missing numbers, ensuring no element from arr is within any range, and every missing number is covered exactly once."""
class Solution:
    def missingRanges(self, arr, lower, upper):
        temp = []
        result = []

        for i in range(lower, upper + 1):
            if i not in arr:
                temp.append(i)
            elif temp != []:
                result.append([temp[0], temp[-1]])
                temp = []

        if temp:
            result.append([temp[0], temp[-1]])

        return result

obj = Solution()
arr = [14, 15, 20, 30, 31, 45]
low = 10
up = 50
print(obj.missingRanges(arr, low, up))