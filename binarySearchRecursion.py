#!/usr/bin/env python
# coding=utf-8


### recursion implements binary search


searchlist=[12,29,32,34,38,42,49,60,66,72,88]
low=0
high=len(searchlist)-1

k=int(raw_input("please input the num u r searching:"))

print str(k)
def binarySearch(ll,hh,list):
   
    if(ll<hh):
         mid=(ll+hh)/2
         if(k<list[mid]):
             return  binarySearch(ll,mid-1,list)   ### 这里调用的时候不能只写函数 ，不return的话无法退出函数体运行下一层。
         elif(k>list[mid]):
             return binarySearch(mid+1,hh,list)
         else:
             return  "found at position:"+str(mid)
    else:
        return 'not found'
print binarySearch(low,high,searchlist)






