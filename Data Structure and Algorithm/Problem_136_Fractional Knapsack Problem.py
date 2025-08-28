"""Given two arrays, val[] and wt[] , representing the values and weights of items, and an integer capacity representing the maximum weight a knapsack can hold, determine the maximum total value that can be achieved by putting items in the knapsack. You are allowed to break items into fractions if necessary.
Return the maximum value as a double, rounded to 6 decimal places."""
class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        n = len(val)
        
        # store (ratio, index) for sorting
        new_array = []
        for i in range(n):
            new_array.append([val[i] / wt[i], i])
        
        # sort by ratio descending
        new_array.sort(reverse=True, key=lambda x: x[0])
        
        final_value = 0.0
        curr_wt = 0
        
        for ratio, j in new_array:
            if curr_wt + wt[j] <= capacity:
                # take the whole item
                curr_wt += wt[j]
                final_value += val[j]
            else:
                # take fraction
                remaining = capacity - curr_wt
                final_value += ratio * remaining
                break
        
        return final_value



obj = Solution()
val = [100,60, 100, 200]
wt = [20, 10, 50, 50]
capacity = 90
print(obj.fractionalKnapsack(val,wt,capacity))
# Output : 380.0