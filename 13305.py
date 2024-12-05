import sys

input = sys.stdin.readline

n = int(input())

distance = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

total = 0
current_oil_price = oil_price[0]
current_distance = 0
i = 0
# print(oil_price)
# print(distance)
# while i is not n - 1:
#     if oil_price[i] < oil_price[i + 1]:  # 도착해서 넣는게 비싸다면
#         print(oil_price[i], "vs ", oil_price[i + 1])
#         print("목적지 기름이 더 비쌈")
#         current_distance += distance[i]
#         print(current_distance, "만큼 거리 적립")
#
#         print("current_oil_price",current_oil_price)
#         # total += oil_price[i] * distance[i]
#         print(total)
#         i += 1
#     else:  # 넣고 가는게 비싸면 (목적지가 더 쌈)
#         print(oil_price[i], "vs ", oil_price[i + 1])
#         print("목적지 기름이 더 쌈")
#         print("현재 모인 거리의 수", current_distance)
#         total += (current_distance + distance[i]) * current_oil_price
#         current_distance = 0
#         print("current_oil_price",current_oil_price)
#         # current_oil_price = oil_price[i]  # 기준 오일 가격을 갱신
#         current_oil_price=oil_price[i+1]
#         print(total)
#         i += 1
# if current_distance != 0:
#     total += current_oil_price * current_distance
for i in range(n - 1):  # 마지막 도시는 이동할 필요가 없으므로 n-1까지만 반복
    total += current_oil_price * distance[i]  # 현재 가격으로 이동 비용 계산
    if oil_price[i + 1] < current_oil_price:  # 다음 도시의 주유소가 더 저렴하면 갱신
        current_oil_price = oil_price[i + 1]
print(total)
