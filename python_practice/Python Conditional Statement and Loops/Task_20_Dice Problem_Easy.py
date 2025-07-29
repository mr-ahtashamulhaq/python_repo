"""You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face of this cube, your task is to guess the number on the opposite face of the cube."""
#User function Template for python3
class Solution:
    def oppositeFaceOfDice(self, n):
        match n:
            case 1:
                return 6
            case 2:
                return 5
            case 3:
                return 4
            case 4:
                return 3
            case 5:
                return 2
            case 6:
                return 1

# obj = Solution()
# print(obj.oppositeFaceOfDice(1))