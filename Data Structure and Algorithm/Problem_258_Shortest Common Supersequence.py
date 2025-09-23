"""Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s."""
class Solution:
    def shortestCommonSupersequence(self, text1: str, text2: str) -> str:
        
        # Finding LCS of both strings
        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for ind1 in range(n1 + 1):
            dp[ind1][0] = 0                        
        for ind2 in range(n2 + 1):
            dp[0][ind2] = 0

        for ind1 in range(1, n1 + 1):
            for ind2 in range(1, n2 + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = 0 + max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        i, j = n1, n2
        result = []
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                result.append(text1[i - 1])
                i -= 1
                j -= 1
            else:
                if dp[i][j - 1] >= dp[i - 1][j]:
                    j -= 1
                else:
                    i -= 1
        result.reverse()
        LCS = "".join(result)   
        
        


        # Shortest Common Supersequence  = st1 + str2 - ( LCS (str1 , str2) )
        string = text2
        my_set = list(LCS)
        for i in text1:
            if i in my_set:

                my_set.remove(i)
            else:
                string += i

        return string


obj = Solution()
str1 = "abac" ;str2 = "cab"

print(obj.shortestCommonSupersequence(str1, str2))

# Output : cabac