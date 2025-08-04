"""Given a number, in the form of an array Num[] of size N containing digits from 1 to 9(inclusive). The task is to find the next smallest palindrome strictly larger than the given number."""

class Solution:
    def nextPalindrome(self, num):
        n = len(num)

        if all(x == 9 for x in num):
            return [1] + [0]*(n-1) + [1]

        left = num[:n//2]
        middle = [num[n//2]] if n % 2 != 0 else []
        new_num = left + middle + left[::-1]

        if new_num > num:
            return new_num

        if n % 2 == 0:
            left_to_add = left
        else:
            left_to_add = left + middle

        i = len(left_to_add) - 1
        while i >= 0:
            if left_to_add[i] < 9:
                left_to_add[i] += 1
                break
            else:
                left_to_add[i] = 0
                i -= 1

        if n % 2 == 0:
            left = left_to_add
            middle = []
        else:
            left = left_to_add[:-1]
            middle = [left_to_add[-1]]

        return left + middle + left[::-1]

obj = Solution()
arr = [9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2]
print(obj.nextPalindrome(arr))