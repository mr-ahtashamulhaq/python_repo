"""You are given a string that represents the prefix form of a valid mathematical expression. Convert it to its postfix form."""
class Solution:
    def preToPost(self, pre_exp):
        # Code here
        result = []
        n = len(pre_exp)
        for i in range(n-1,-1,-1):
            char = pre_exp[i]

            if char.isalnum():
                result.append(char)

            else:
                last = result.pop()
                second_last = result.pop()

                tempstring = last + second_last + char

                result.append(tempstring)

        return result[0]

obj =   Solution()
s = "*-A/BC-/AKL"
print(obj.preToPost(s))

# Output: ABC/-AK/L-*