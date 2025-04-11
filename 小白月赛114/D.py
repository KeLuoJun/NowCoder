# from collections import *
# from functools import cache
def ln(): return int(input())
def lnums(): return list(map(int,input().split()))
def slv():
    n,k=lnums()
    nums=lnums()
    t=n
    for i in range(n):
        if k>=i:
            k-=i-1
        else:
            t=i
            break
    nums+=[0]
    mn=0xffffffffffffff
    for i in range(1,n):
        nums[i]+=nums[i-1]
    s=nums[-2]
    tmp=[0]*n 
    tmp[n-1]=s 
    for i in range(n-2,-1,-1):
        tmp[i]=min(nums[i],tmp[i+1])
    for i in range(t+1):
        mn=min(mn,tmp[i+n-1-t]-nums[i-1])
    return max(s-mn,0)
print(slv())