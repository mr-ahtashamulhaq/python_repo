"""There are two parallel roads, each containing n and m buckets, respectively. Each bucket may contain some balls. The balls in the first road are given in an array a of size n and balls in the second road in an array b of size m. The buckets on both roads are kept in such a way that they are sorted according to the number of balls in them. Geek starts from the left side of the road.Geek can change the road only at a point of intersection i.e. a point where buckets have the same number of balls on two roads. Help Geek collect the maximum number of balls."""
#User function Template for python3
class Solution:
    def maxBalls(self, n, m, a, b):
        size = n if n>m else m
        sum = 0
        for i in range (0,size):
            if a[i]==b[i]:
                sum += a[i]
            elif a[i]>b[i]:
                sum += a[i]
            elif a[i]<b[i]:
                sum+=b[i]
        return sum
obj = Solution()
arr1 = [2,4,6,7]
arr2 = [1,6,8,3]
print(obj.maxBalls(4,4,arr1,arr2))