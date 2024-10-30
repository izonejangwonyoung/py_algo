n,m=map(int,input().split())
list_num=sorted(list(map(int,input().split())))
ans=[]



def back():
    if len(ans)==m:
        print(" ".join(map(str,ans)))
        return
    for i in list_num:
        if len(ans)==0 or ans[-1]<=i:
            ans.append(i)
            back()
            ans.pop()

back()