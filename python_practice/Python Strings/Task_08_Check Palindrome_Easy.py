"""Given a string s, you need to check if it is palindrome or not. A palidrome is a string that reads the same from front and back."""
def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

print(isPalindrome("racecar"))
    