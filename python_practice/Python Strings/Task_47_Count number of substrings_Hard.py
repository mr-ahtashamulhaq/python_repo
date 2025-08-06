"""You are given a string consisting of lowercase characters and an integer k, You have to count all possible substrings that have exactly k distinct characters. """
class Solution:
    def countSubstrWithKDistinct(self, s, k):
        n = len(s)
        count = 0
        
        for i in range(n):
            unique_chars = set()
            for j in range(i, n):
                unique_chars.add(s[j])
                if len(unique_chars) == k:
                    count += 1
                elif len(unique_chars) > k:
                    break
        return count


obj = Solution()
print(obj.countSubstrWithKDistinct("abcbaa", 3))