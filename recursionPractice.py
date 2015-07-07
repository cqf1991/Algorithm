#!/usr/bin/env python
# coding=utf-8
### 一个蛋疼简单的递归


def exR(n):
    if n<=0:
        return ''
    return exR(int(n)-3),n,exR(int(n)-2),n
###   answer 3 1 1 3 6 1 1 4 2 2 6

###print exR('6')


import math

def RECcalcLN(x):
    if x==0:
        return 1
    return  x*RECcalcLN(x-1)


print math.log(RECcalcLN(2))
