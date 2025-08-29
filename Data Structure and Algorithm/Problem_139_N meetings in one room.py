#User function Template for python3

class Solution:
    def maximumMeetings(self,start,end):
        
        end_start_list = []
        for i in range(len(start)):
            end_start_list.append([end[i] , start[i]])
        end_start_list.sort()

        last_end = end_start_list[0][0]
        total_meetings= 1
        for i in range(1, len(end_start_list)):
            if end_start_list[i][1] > last_end:
                total_meetings +=1
                last_end = end_start_list[i][0]

        return total_meetings

obj = Solution()
start = [1, 3, 0, 5, 8, 5]
end =  [2, 4, 6, 7, 9, 9]
print(obj.maximumMeetings(start, end))
# Output : 4