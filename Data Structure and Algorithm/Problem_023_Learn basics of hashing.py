"""Given list M count how many times every element present in N
 Note :  1<=n[i]<=10"""

class Solution:
    def hashmap(self,N,M):
        final_dict = {}
        hash_map = [0] * 11
        for num in N:
            hash_map[num] +=1
        for i in M:
            if i<1 or i>10:
                final_dict[i] = 0
            else:
                final_dict[i] = hash_map[i]
        return final_dict
        
N = [1,2,5,1,7,2,1,1,5,9,3,5,5,4,4]
M = [1,2,3,4,5,11]

obj = Solution()
print(obj.hashmap(N,M))

# Output : {1: 4, 2: 2, 3: 1, 4: 2, 5: 4, 11: 0}