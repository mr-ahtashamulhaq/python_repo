"""Given an input stream s consisting only of lowercase alphabets. While reading characters from the stream, you have to tell which character has appeared only once in the stream upto that point. If there are many characters that have appeared only once, you have to tell which one of them was the first one to appear. If there is no such character then append '#' to the answer."""

class Solution:
    def FirstNonRepeating(self, s):
        result = ''
        count = {}  
        queue = []  

        for ch in s:
            count[ch] = count.get(ch, 0) + 1
            if count[ch] == 1:
                queue.append(ch)


            while queue and count[queue[0]] > 1:
                queue.pop(0)

            if queue:
                result += queue[0]
            else:
                result += '#'

        return result

obj = Solution()
s = "aabc"
print(obj.FirstNonRepeating(s)) 