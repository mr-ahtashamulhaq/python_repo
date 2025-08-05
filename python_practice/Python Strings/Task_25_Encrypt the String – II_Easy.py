"""You are given a string S. Every sub-string of identical letters is replaced by a single instance of that letter followed by the hexadecimal representation of the number of occurrences of that letter. Then, the string thus obtained is further encrypted by reversing it [ See the sample for more clarity ]. Print the Encrypted String."""
class Solution:
    def encryptString(self, S):
        res = ""
        count = 1

        for i in range(len(S)):
            if i < len(S) - 1 and S[i] == S[i+1]:
                count += 1
            else:
                hex_count = format(count, 'x')
                res += S[i] + hex_count
                count = 1
        
        res = res[::-1]
        
        return res

obj = Solution()
print(obj.encryptString("aaaaaaaaaaa"))