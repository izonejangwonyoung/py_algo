import heapq
import sys
input=sys.stdin.readline
heap=[]
n=int(input())
for i in range(n):
    num=int(input())
    if num!=0:
        heapq.heappush(heap,(-num,num))
    else:  #0일 경우. 즉 배열에서 가장 큰 값을 출력하고 해당 값을 제거
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])