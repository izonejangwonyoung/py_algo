import re

expression = input()
parts = re.findall(r'\d+|-', expression)

# print(parts)
num_sum = 0
index = 0
temp = 0

while index < len(parts):
    # print(index)
    if parts[index] == '-':
        # print("-발견")
        index += 1
        while index < len(parts) and parts[index] != '-':
            # print(parts[index], "검사중")
            temp += int(parts[index])
            index += 1
            # print(index, "진행")
        num_sum = num_sum - temp
        temp=0
    else:
        num_sum += int(parts[index])
        index += 1

print(num_sum)
