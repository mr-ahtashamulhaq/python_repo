"""Given a queue of persons represented by an array of integers, where each person is identified by a specific integer, find the minimum kilograms of apples that need to be distributed, ensuring that each person receives 1 kilogram of apples only once."""
class Solution:
    def minimumApple(self, arr):
        return len(set(arr))

obj = Solution()   
arr = [1, 2, 2, 3, 4, 1, 5]
print(obj.minimumApple(arr))