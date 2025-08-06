"""Given a string S that consists of only alphanumeric characters and dashes. The string is separated into N + 1 groups by N dashes. Also given an integer K. 

We want to reformat the string S, such that each group contains exactly K characters, except for the first group, which could be shorter than K but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted string."""
class Solution:
    def ReFormatString(self, S, K):
        S = S.replace("-", "").upper()
        
        first_group_len = len(S) % K
        if first_group_len == 0:
            first_group_len = K
        
        groups = [S[:first_group_len]]
        
        i = first_group_len
        while i < len(S):
            groups.append(S[i:i+K])
            i += K
        
        return "-".join(groups)


obj = Solution()
print(obj.ReFormatString("746-3736-84-84-847", 4))