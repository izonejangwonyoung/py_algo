# import sys
# input = sys.stdin.readline
# m = int(input())
#
# def back(start):
#     global cnt
#
#     if start==m:
#         cnt+=1
#     else:
#         for i in range(m):
#             row[start]=i
#             if not attack(start):
#                 back(start+1)
#
# def attack(x):
#     for i in range(x):
#         if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
#             return True
#     return False
#
# row = [0] * m
# cnt = 0
# back(0)
#
# print(cnt)