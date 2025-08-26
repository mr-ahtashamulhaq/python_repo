"""We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet."""
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []
        for i in range(n):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                while len(stack) != 0 and stack[-1] > 0 and  abs(asteroids[i]) > stack [-1]:
                    stack.pop()

                if len(stack) != 0 and abs(asteroids[i]) == stack[-1]:
                    stack.pop()
                elif len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroids[i])

        return stack

                
obj = Solution()
nums = [5,10,-5]
print(obj.asteroidCollision(nums))
# Output :[5, 10]