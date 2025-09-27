from typing import List, Optional
class Solution:
    #USING RECURSION
    
    # This take index and return length on longest chain till this index
    def recursion(self, ind, words, hashmap ) : 
        if ind >= len(words) :
            return 0


        result = 1          # every word alteast have 1 length chain of its own

        for j, ch in enumerate(words[ind]) :
            w = words[ind]

            predecessor = w[ : j] + w[ j+1 : ]
            if predecessor in hashmap :        # This word exist in our given list in question
                result = max(result ,  1 + self.recursion(hashmap[predecessor], words, hashmap) )

        return result

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda w : - len(w) ) # Length in negative so it could sort in negative

        hashmap = {}        # Hash index of every word with its index as value

        for i, word in enumerate(words): 
            hashmap[word] = i
        
        ans = 1
        for j in range(len(words)) :
            ans = max(ans , self.recursion(j, words, hashmap))
        return ans
    
    
    
    
    
    
    #USING MEMOIZATION
    def memoization(self, ind, words, hashmap, dp) : 
        if ind >= len(words) :
            return 0

        if ind in dp :
            return dp[ind]

        result = 1 

        for j, ch in enumerate(words[ind]) :
            w = words[ind]

            predecessor = w[ : j] + w[ j+1 : ]
            if predecessor in hashmap :        
                result = max(result ,  1 + self.memoization(hashmap[predecessor], words, hashmap, dp) )

        dp[ind] = result
        return dp[ind]

    def longestStrChain_memo(self, words: List[str]) -> int:
        words.sort(key = lambda w : - len(w) ) 

        hashmap = {}        

        for i, word in enumerate(words): 
            hashmap[word] = i
        
        ans = 1
        dp = {}         # will store key = index  and value = longest length till this index
        for j in range(len(words)) :
            ans = max(ans , self.memoization(j, words, hashmap, dp))
        return ans
        
obj = Solution()
words = ["a","b","ba","bca","bda","bdca"]
print( obj.longestStrChain(words) )
print( obj.longestStrChain_memo(words) )


