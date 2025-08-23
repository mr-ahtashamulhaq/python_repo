"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters."""
class Solution:
    #Helper
    def solve(self,ind,subset,char_map,digits,result):
        if ind >= len(digits):
            result.append("".join(subset))
            return

        for ch in (char_map[digits[ind]]):
            subset.append(ch)
            self.solve(ind+1,subset,char_map,digits,result)
            subset.pop()

    #main 
    def letterCombinations(self, digits: str):
        char_map = {"2" : "abc",
                    "3" : "def",
                    "4" : "ghi",
                    "5" : "jkl",
                    "6" : "mno",
                    "7" : "pqrs",
                    "8" : "tuv",
                    "9" : "wxyz" }
        if digits == "":
            return []
        result = []
        self.solve(0,[],char_map,digits,result)
        return result

obj = Solution()
print(obj.letterCombinations("46"))
# Output: ['gm', 'gn', 'go', 'hm', 'hn', 'ho', 'im', 'in', 'io']