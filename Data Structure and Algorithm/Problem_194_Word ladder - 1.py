"""A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists."""
from typing import List, Optional
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:   
        #Convert into set to check in O(1)
        wordset= set(wordList)

        # if end not exist early return
        if endWord not in wordset:
            return 0
        
        queue = deque()
        queue.append((beginWord,1))

        while len(queue) != 0:
            curr_word , level  = queue.popleft()

            if curr_word == endWord:
                return level
            
            #for every word change its every letter one by one and check if it is in our wordlist if yes it could be our path 
            for i in range(len(curr_word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if ch == curr_word[i]:
                        continue
                    new_word = curr_word[:i] + ch + curr_word[i+1:]
                    if new_word in wordset:
                        queue.append((new_word, level+1))
                        wordset.remove(new_word)
        return 0

obj = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print( obj.ladderLength(beginWord , endWord, wordList ) )