"""Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number."""
class Solution:
    def findContentChildren(self, g, s) :
        right = 0
        left = 0
        count = 0
        s.sort()
        g.sort()
        while right < len(s) and left < len(g):
            if g[left] <= s[right]:
                count +=1
                left +=1
            right +=1


        return count
    
obj = Solution()
g = [1,2,3]
s = [1,1]
print(obj.findContentChildren(g,s))
# Output  : 1