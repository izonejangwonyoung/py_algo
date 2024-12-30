from operator import index

num_list=list(map(int,input().split()))
num_count=[]
prize=0
for i in range(0,3):
    num_count.append(num_list.count(num_list[i]))
# print(num_count)
if 2 in num_count: #같은 숫자가 1번 이상 나오는 경우
    prize=1000+num_list[num_count.index(2)]*100
elif 3 in num_count:
    prize=10000+num_list[num_count.index(3)]*1000
else:
    prize=max(num_list)*100
print(prize)