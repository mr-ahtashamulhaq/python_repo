"""Given a non-negative integer(without leading zeroes) represented as an array arr. Your task is to add 1 to the number (increment the number by 1). The digits are stored such that the most significant digit is at the starting index of the array."""
class Solution:
    def addOne(self, arr):
        number = 0
        li = []
        for k,i in enumerate(arr[::-1]):
            number += i*(10**k)
        number += 1
        for i in str(number):
            li.append(i)
        return li


obj = Solution()
arr = [9,9,9]
print(obj.addOne(arr))