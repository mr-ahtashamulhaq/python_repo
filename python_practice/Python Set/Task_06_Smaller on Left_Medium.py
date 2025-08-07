"""Given an array arr[ ] of n positive integers, the task is to find the greatest element on the left of every element in the array which is strictly smaller than itself, if this element does not exist for an index print "-1"."""

def greatest_smaller_on_left(arr):
    result = []
    for i in range(len(arr)):
        max_smaller = -1
        for j in range(i):
            if arr[j] < arr[i]:
                max_smaller = max(max_smaller, arr[j])
        result.append(max_smaller)
    return result

arr = [2, 5, 3, 7, 1, 9]
print(greatest_smaller_on_left(arr))  