"""You are given two numbers a and b. Your task is to swap the given two numbers.

Note: Try to do it without a temporary variable."""
class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b


s = Solution()
p = s.get(3, 5)
print(p[0], p[1])  
#Output: 5 3