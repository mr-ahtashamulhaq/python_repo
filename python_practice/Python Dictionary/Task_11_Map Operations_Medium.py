"""You are given an array arr. You need to insert the elements of arr into a map(index as key and element as values). 
Also, you need to erase a given element x from the map and print "erased x" if successfully erased.
else print "not found".

Complete print() function to print the map."""

class Solution:
    def map_operation(self, arr,x):
        dict = {}
        for i in range(len(arr)//2):
            dict[arr[i]] = arr[i+(len(arr)//2)]
        
        print("KEY VALUES:")
        print(dict)
        dict.pop(x)
        print("\nERASED")
        print(dict)
        pass

obj = Solution()
# array with index and values
arr = [0,1,2,3,4,5,6,7,906,756,348,826,496,350,726,681]
x = 3
obj.map_operation(arr,x)