"""Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number. Given a number N, the task is to check if it is a Strong Number or not. Print 1 if the Number is Strong, else Print 0."""
#User function Template for python3
class Solution:
    def isStrong(self, N):
        originalN = N
        li = list(str(N))
        sum = 0
        for j in li:
            fact=1
            for i in range(1,int(j)+1):
                fact*=i
            sum += fact
        return 1 if sum==originalN else 0

obj =Solution()
print(obj.isStrong(14))