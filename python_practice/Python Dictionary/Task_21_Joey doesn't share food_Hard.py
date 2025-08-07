"""Every friends fan know that joey loves food and monica loves to cook. So, on a occassion of thanksgiving monica made n types of food containing exactly 6 ingredients each. Monica is an excellent cook so she can cook food by adding any ingredient at any order. All ingredients contains protein on the scale of 1 to 10^6. Now, Chandler invented the fun game where everyone needs to find the successive protein rate in all n food of the ingredient on the top(6th ingredient is on top). Ross being the most curious wants to finish this game before dinner, so he wants your help to complete the task."""

class Solution:
    def topIngredients(self, foods):
        tops = []
        for food in foods:
            tops.append(food[5])
        return tops


foods = [
    [3, 5, 2, 7, 1, 9],
    [10, 2, 6, 4, 8, 3],
    [9, 1, 2, 3, 4, 5]
]

sol = Solution()
print(sol.topIngredients(foods))