numbers = []
answers = []
temp = []
while True:
    number = int(input())
    if number == -1:
        break
    numbers.append(number)

for i in numbers:
    for j in range(1, i):
        if i % j == 0:
            temp.append(j)
    if sum(temp) == i:
        print(str(i) + " = ", end='')
        for k in temp:
            if k == temp[-1]:
                print(k, end="\n")  # 마지막 요소에는 + 출력 안 함
            else:
                print(k, end=" + ")
    else:
        print(f"{i} is NOT perfect.")
    temp = []
