n=int(input())

way=[]
def calc(n,origin,sub,dest):
    if n==1:
        way.append([origin,dest])
        return
    calc(n-1,origin,dest,sub)
    way.append([origin,dest])
    calc(n-1,sub,origin,dest)






calc(n,1,2,3)
print(len(way))
for i in range(len(way)):
    print(way[i][0],way[i][1])