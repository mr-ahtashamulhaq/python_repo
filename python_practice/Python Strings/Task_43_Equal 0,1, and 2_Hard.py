"""Given a string str of length N which consists of only 0, 1 or 2s, count the number of substring which have equal number of 0s, 1s and 2s."""
class Solution:
    def getSubstringWithEqual012(self, Str):
        count = 0
        n = len(Str)

        for i in range(n):
            for j in range(i, n):
                sub = Str[i:j+1]
                c0 = c1 = c2 = 0

                for ch in sub:
                    if ch == '0':
                        c0 += 1
                    elif ch == '1':
                        c1 += 1
                    elif ch == '2':
                        c2 += 1

                if c0 == c1 == c2 and c0 != 0:
                    count += 1
                    
        return count


obj = Solution()
print(obj.getSubstringWithEqual012("11100022"))