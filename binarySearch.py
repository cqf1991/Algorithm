#!/usr/bin/env python
# coding=utf-8

### binary search by python

searchlist=[12,29,32,34,38,42,49,60,66,72,88]
low=0
high=len(searchlist)-1
print low,high ### searchlist.__len__()     can also get length of list

k=int(raw_input("please input the num u r searching:"))

while(low<=high):
    mid=(low+high)/2
    if k<searchlist[mid]:
        high=mid-1   ### 1,2,3,4,5     find 2 in 12345->find 2 in 12-> find 2
    elif k>searchlist[mid]:
        low=mid+1
    else:
        if k==searchlist[mid]:
            print 'find at position:',mid
            break

    if low>high:
        print 'not found'
