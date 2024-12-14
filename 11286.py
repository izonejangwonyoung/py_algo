import sys
import heapq
input=sys.stdin.readline



n=int(input())
heap=[]
for i in range(n):
    tmp=int(input())
    if tmp!=0:
        heapq.heappush(heap,(abs(tmp),tmp))
    else:
        if len(heap)==0:
            print(0)
        else:
            result=heapq.heappop(heap)[1]
            print(result)


