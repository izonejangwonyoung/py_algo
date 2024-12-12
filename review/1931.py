n=int(input())

timetable=[]



for i in range(n):
    timetable.append(list(map(int,input().split())))
timetable=sorted(timetable, key = lambda x:(x[1],x[0]))
# print(timetable)
count=1
curr_meeting_end=timetable[0][1]
for i in range(1,n):
    # print(timetable[i][0])
    if timetable[i][0]>=curr_meeting_end:   #기존 회의 종료 시간이 다음 회의 시작 시간과 같거나, 작은 경우
        # print(timetable[i])
        curr_meeting_end=timetable[i][1]
        count+=1

print(count)