"""Given an array arr of N integers, the task is to replace each element of the array by its rank in the array. The rank of an element is defined as the distance between the element with the first element of the array when the array is arranged in ascending order. If two or more are same in the array then their rank is also the same as the rank of the first occurrence of the element. """

import heapq
class Solution:
    def replaceWithRank(self, N, arr):


        heap = list(set(arr))
        heapq.heapify(heap)
        
        rank_map = {}
        rank = 0
        
        while heap :
            val = heapq.heappop(heap)
            rank_map [val]  = rank+1 
            rank +=1
        result = []  
        for key in arr:
            result.append(rank_map[key])
        return result

obj =Solution()
N = 6
arr = [20, 15, 26, 2, 98, 6]
print(obj.replaceWithRank(N ,arr))

# Output  : [4, 3, 5, 1, 6, 2]