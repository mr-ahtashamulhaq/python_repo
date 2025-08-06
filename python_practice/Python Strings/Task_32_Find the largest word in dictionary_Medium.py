"""Given a string s and a string dictionary d, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string"""
class Solution:
    def findLongestWord(self, s, dictionary):
        best_word = ""
        
        for word in dictionary:
            i = 0 
            j = 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            
            if j == len(word):
                if len(word) > len(best_word) or (len(word) == len(best_word) and word < best_word):
                    best_word = word
        
        return best_word


obj = Solution()
s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]
print(obj.findLongestWord(s, dictionary))