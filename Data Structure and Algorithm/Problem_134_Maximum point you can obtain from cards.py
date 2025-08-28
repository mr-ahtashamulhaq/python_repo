"""There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain."""
from typing import List
class Solution:
    def maxScore(self, cardpoints: List[int], k: int) -> int:
        n = len(cardpoints)
        result = 0
        left_sum = 0
        right_sum = 0

        for i in range(0,k):
            left_sum += cardpoints[i]
        
        result = left_sum
        right_index = n-1

        for i in range(k-1, -1 , -1):
            left_sum -= cardpoints[i]
            right_sum += cardpoints[right_index]
            result  = max(result, left_sum + right_sum)

            right_index -=1


        return result

obj = Solution()
cardpoints = [1,2,3,4,5,6,1]
k = 3
print(obj.maxScore(cardpoints , k))
# Output : 12