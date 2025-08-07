"""Given an array arr of N integers, the task is to check whether the frequency of the elements in the array is unique or not. Or in other words, there are no two distinct numbers in array with equal frequency. If all the frequency is unique then return true, else return false"""
def isFrequencyUnique(arr):
    freq = {}
    
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    freq_values = list(freq.values())
    return len(freq_values) == len(set(freq_values))

arr = [1,2,2,3,3,3,4,4,4,4]
print(isFrequencyUnique(arr))