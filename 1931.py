import sys
input = sys.stdin.readline
n = int(input())
count = 1
meet_time = []

for i in range(n):
    meet_time.append(list(map(int, input().split())))
meet_time.sort(key=lambda x: (x[1], x[0]))# print(meet_time)
# maximum = 1
# print(meet_time)
# for i in range(n-1):
#     start_time = meet_time[i][0]
#     end_time = meet_time[i][1]
#     for j in range(i+1,n):
#         # print("회의 종료 시간",meet_time[i],", 회의 시작 시간 ",meet_time[j]," 검사중")
#         # print(start_time, end_time)
#         if end_time <= meet_time[j][0]:
#             maximum += 1
#             end_time = meet_time[j][1]
#             # print("endtime=",end_time)
#     if real_max < maximum:
#         real_max = maximum
#     # print("현재 계산해서 나온 횟수:",maximum)
#     # print("지금까지 최대 횟수:",real_max)
#     maximum = 1
#     # print("---------------------------")
# print(real_max)
end_time=meet_time[0][1]
for i in range(1,n):
    if meet_time[i][0] >= end_time:
        count += 1
        end_time = meet_time[i][1]
print(count)