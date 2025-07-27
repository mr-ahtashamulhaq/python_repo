"""A series with same common difference is known as arithmetic series. The first term of series is 'a' and common difference is d. The series looks like a, a + d, a + 2d, a + 3d, . . . Find the sum of series upto nth term."""
#User function Template for python3

class Solution:
	def sum_of_ap(self, n, a, d):
		# Code here
		sum = 0
		for i in range(n):
			sum += a + (i*d)
		return sum