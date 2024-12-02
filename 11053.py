a = int(input())
num_list = list(map(int, input().split()))

length = [1] * a
for i in range(len(num_list)):
    length[i]=1
    for j in range(0,i):
        if num_list[j] < num_list[i]:
            length[i]=max(length[i],length[j]+1)


print(max(length))