"""Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise."""
from typing import List
import  heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize !=0 :
            return False

        hash_map= {}
        for n in hand:
            hash_map[n] = hash_map.get(n , 0) +1

        heap = list(hash_map.keys())

        heapq.heapify(heap)

        while heap:
            first = heap[0]
            for i in range(first , first + groupSize):
                if i not in hash_map:
                    return False
                hash_map[i] -=1

                if hash_map[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True
                 
obj = Solution()
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(obj.isNStraightHand(hand , groupSize))
# Output : True