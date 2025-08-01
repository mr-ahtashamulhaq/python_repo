# """Geek is very fond of patterns. Once, his teacher gave him a star pattern to solve. He gave Geek an integer n and asked him to build a pattern."""
#                          * 
#                         * * 
#                        * * * 
#                        * * * 
#                         * * 
#                          * 


class Solution:
    def printDiamond(self, N):
        print()
        for i in range(1,N+1):
            print(" "*((N+1)-i), "* "*i )
        for i in range(N,0,-1):
            print(" "*((N+1)-i), "* "*i )

obj = Solution()
obj.printDiamond(3)