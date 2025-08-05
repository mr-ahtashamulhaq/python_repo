"""Given a list of words, S followed by two specific words, word1 and word2, the task is to find the minimum distance between the indices of these two words in the list.

Note: word1 and word2 are both in the list, and there can be multiple occurrences of words in the list."""
class Solution:
    def shortestDistance(self, s, word1, word2):
        indices1 = [i for i, word in enumerate(s) if word == word1]
        indices2 = [i for i, word in enumerate(s) if word == word2]
        
        min_dist = float('inf')
        
        for i in indices1:
            for j in indices2:
                dist = abs(i - j)
                if dist < min_dist:
                    min_dist = dist
        
        return min_dist

obj = Solution()
words = ["practice", "makes", "perfect", "coding", "makes"]
print(obj.shortestDistance(words, "coding", "practice")) 