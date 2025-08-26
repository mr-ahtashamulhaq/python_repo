"""You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its prefix form."""
#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        # Code here
        result = []
        for i in range(len(post_exp)):
            char = post_exp[i]

            if char.isalnum():
                result.append(char)
            #when found operator
            else:
                last = result.pop()
                second_last = result.pop()
                tempstring  = char + second_last + last
                result.append(tempstring)

        return result[0]
    
obj =Solution()
s = "ABC/-AK/L-*"
print(obj.postToPre(s))
    
# Output : *-A/BC-/AKL