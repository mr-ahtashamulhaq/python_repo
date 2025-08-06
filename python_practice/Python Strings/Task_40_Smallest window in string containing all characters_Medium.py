"""Given two strings s1 and s2. Find the smallest length in the string s1 consisting of all the characters(including duplicates) of the string s2. return empty string in case no such length is present.

Note: All characters are in lowercase letters. """
class Solution:
    def smallestWindow(self, s1, s2):
        n = len(s1)
        m = len(s2)
        min_len = float('inf')
        result = ""

        for i in range(n):
            if s1[i] == s2[0]:
                temp = ""
                needed = list(s2)
                for j in range(i, n):
                    temp += s1[j]
                    if s1[j] in needed:
                        needed.remove(s1[j])
                    if not needed:  
                        if len(temp) < min_len:
                            min_len = len(temp)
                            result = temp
                        break

        return result if result else ""


obj = Solution()
print(obj.smallestWindow("timetopractice", "toc"))