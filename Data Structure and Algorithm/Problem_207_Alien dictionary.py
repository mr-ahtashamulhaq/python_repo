"""A new alien language uses the English alphabet, but the order of letters is unknown. You are given a list of words[] from the alien language’s dictionary, where the words are claimed to be sorted lexicographically according to the language’s rules.

Your task is to determine the correct order of letters in this alien language based on the given words. If the order is valid, return a string containing the unique letters in lexicographically increasing order as per the new language's rules. If there are multiple valid orders, return any one of them.

However, if the given arrangement of words is inconsistent with any possible letter ordering, return an empty string ("").

    A string a is lexicographically smaller than a string b if, at the first position where they differ, the character in a appears earlier in the alien language than the corresponding character in b. If all characters in the shorter word match the beginning of the longer word, the shorter word is considered smaller.

Note: Your implementation will be tested using a driver code. It will print true if your returned order correctly follows the alien language’s lexicographic rules; otherwise, it will print false."""

from collections import deque
class Solution:
    def findOrder(self, words):

        #Make unique characters list
        seen = set()
        unique=[]
        for word in words:
            for ch in word:
                if ch not in seen:
                    seen.add(ch)
                    unique.append(ch)

        # Make adj_list of unique character as key , and their value as set so when we append in it the duplicates auto remove
        adj_list = {ch : set() for ch in unique}
        indegree = {ch : 0 for ch in unique}

        # now find the first unmatched character in two words when find add it in adj_list
        for i in range(len(words)-1):
            word1 , word2 = words[i] , words[i+1]
            if len(word1) > len(word2) and word1.startswith(word2):
                return "" 

            length = len(word1) if len(word1) < len(word2) else len(word2)
            
            for j in range(length):
                if word1[j] != word2[j]:
                    if word2[j] not in adj_list[word1[j]]:
                        adj_list[word1[j]].add(word2[j])
                        indegree[word2[j]] +=1
                    break
            
        # Simle Kahn's ALgorithm
        queue = deque()
        visited = {ch : 0 for ch in unique}
        for key in indegree:
            if indegree[key] == 0:
                queue.append(key)
                visited[key] = 1

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)

            for adjNode in adj_list[node]:
                indegree[adjNode] -=1
                if indegree[adjNode] == 0:
                    queue.append(adjNode)

        if len(result) == len(adj_list):
            return result
        else:
            return ""


obj = Solution()
words = ["baa", "abcd", "abca", "cab", "cad"]
print( obj.findOrder(words) )
# Output : ['b', 'd', 'a', 'c']