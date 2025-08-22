"""Given a pair of strings s1 and s2 of equal lengths, your task is to find which of the two strings has more distinct subsequences. If both strings have the same number of distinct subsequences, return s1."""
#User function Template for python3
class Solution:
    def subsequences(self,ind,string,temp,result):

        if ind >=len(string):
            copyoftemp  = "".join(temp.copy())
            if copyoftemp not in result and copyoftemp != "":
                result.append(copyoftemp)
            return
        
        temp.append( string[ind])
        self.subsequences(ind+1, string,temp,result)

        temp.pop()

        self.subsequences(ind+1,string,temp,result)
        return result




    def betterString(self, s1, s2):
        result = []
        n = len(s1)
        temp = []
        s1result = self.subsequences(0,s1,temp,result)
        result = []
        temp = []
        s2result = self.subsequences(0,s2,temp,result)

        return s1 if len(s1result) > len(s2result) else s2 if  len(s1result) < len(s2result) else s1 #type: ignore
    
obj = Solution()
print(obj.betterString("gboubwd" ,"bekoilx"))
# Output : bekoilx