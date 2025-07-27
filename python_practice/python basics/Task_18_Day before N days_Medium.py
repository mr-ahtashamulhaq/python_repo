"""Given two integers d and n. Where d is the day, out of 7 days of the week, d varies from 0 to 6 as shown below.
0 - Sunday
1 - Monday
2 - Tuesday
3 - Wednesday
4 - Thursday
5 - Friday
6 - Saturday

You have to return the index for the day which is n days before the given day d."""
class Solution:
    def findAnswer(self, d, n): 
       #Code here
       if d > n:
           return d - n
       else:
           n = n%7
           return (d+7) - n