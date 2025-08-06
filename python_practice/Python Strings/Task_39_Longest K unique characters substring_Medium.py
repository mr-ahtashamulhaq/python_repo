"""You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters."""
class Solution:
    def longestKSubstr(self, s, k):
        left = 0
        max_len = -1
        freq = {}
        
        for right in range(len(s)):

            freq[s[right]] = freq.get(s[right], 0) + 1


            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            
            
            if len(freq) == k:
                max_len = max(max_len, right - left + 1)
        
        return max_len


obj = Solution()
print(obj.longestKSubstr("aabbcc", 2))