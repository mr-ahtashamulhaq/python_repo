"""Given an array of strings strs, group the anagrams together. You can return the answer in any order."""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        result = []
        # sort every string and check if it exist as a key in dictionary
        for string in strs:
            sorted_word = ''.join(sorted(string))
            if sorted_word not in dictionary:
                # if not create its value (empty list)
                dictionary[sorted_word] = []

            #then append unsorted word to that  list on its sorted key 
            dictionary[sorted_word].append(string)

        result = list(dictionary.values())
        return result
    
obj = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(obj.groupAnagrams(strs))
# Output : [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] 