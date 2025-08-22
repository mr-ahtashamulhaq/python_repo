"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses."""
class Solution:
    def solve(self,ind,total,brackets,result):

        if ind >= len(brackets):
            if total == 0:
                result.append("".join(brackets))
            return
        
        if total > len(brackets)//2:
            return
        # To remove un accepted cases e.g if start with closing brackets ")"
        if total < 0:
            return
        
        brackets[ind] = "("
        currsum= total +1
        self.solve(ind+1, currsum, brackets,result )

        brackets[ind] = ")"
        currsum = total -1
        self.solve(ind+1, currsum, brackets,result)

    def generateParenthesis(self, n: int):
        brackets = [""] * (n*2)
        result = []
        self.solve(0,0,brackets,result)
        return result



obj = Solution()
print(obj.generateParenthesis(3))
# Output : ['((()))', '(()())', '(())()', '()(())', '()()()']