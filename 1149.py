import sys

input = sys.stdin.readline
n = int(input())
house_rgbcost = []

for _ in range(n):
    house_rgbcost.append(list(map(int, input().split())))

prev_red, prev_green, prev_blue = house_rgbcost[0]
for i in range(1,n):
    curr_red = min(prev_green, prev_blue) + house_rgbcost[i][0]
    curr_green = min(prev_red, prev_blue) + house_rgbcost[i][1]
    curr_blue = min(prev_red, prev_green) + house_rgbcost[i][2]
    prev_red, prev_green, prev_blue = curr_red, curr_green, curr_blue

print(min(curr_red, curr_blue, curr_green))