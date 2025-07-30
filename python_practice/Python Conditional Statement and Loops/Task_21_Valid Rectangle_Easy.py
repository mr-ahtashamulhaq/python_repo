"""Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping. (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle)."""
#User function Template for python3
class Solution:
    
    def doOverlap(self, L1, R1, L2, R2):
        if R1[0]<L2[0] or R2[0]<L1[0] or L2[1]<R1[1] or L1[1]<R2[1]:
            return 0
        else:
            return 1
 
                    

obj = Solution()
L1  = [5,15]
R1  = [15,5]
L2  = [5,10]
R2  = [10,5]
print(obj.doOverlap(L1,R1,L2,R2))