"""Given an integer n. Return the nth row of the following look-and-say pattern.
1
11
21
1211
111221
Note:
To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit.
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
"""

class Solution:
    def lookAndSay(self, n):
        result = "1"
        
        for _ in range(1, n):
            new_result = ""
            count = 1
            
            for i in range(1, len(result) + 1):
                if i < len(result) and result[i] == result[i - 1]:
                    count += 1
                else:
                    new_result += str(count) + result[i - 1]
                    count = 1
            
            result = new_result
        
        return result


obj = Solution()
print(obj.lookAndSay(5))