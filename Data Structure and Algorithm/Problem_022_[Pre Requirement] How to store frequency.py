"""Given array 'nums' store its frequency in a dictionary/hashmap"""
class Solution:
    def hashmap(self,nums : list):
        hash_map = {}
        for i in range(0,len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]] +=1
            else:
                hash_map[nums[i]] = 1
        return hash_map
obj = Solution()
nums = [1,2,7,3,1,1,2,2,2,7,8,5,2,3,4]
print(obj.hashmap(nums))
# Output : {1: 3, 2: 5, 7: 2, 3: 2, 8: 1, 5: 1, 4: 1}


#Method 2
class Solution2:
    def hashmap(self,nums : list):
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i],0) + 1
        return hash_map

obj = Solution2()
nums = [1,2,7,3,1,1,2,2,2,7,8,5,2,3,4]
print(obj.hashmap(nums))
# Output : {1: 3, 2: 5, 7: 2, 3: 2, 8: 1, 5: 1, 4: 1}