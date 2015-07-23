#!/usr/bin/env python
# coding=utf-8


### implement linklist by python

class Node:
    next=None
    data=None
    def __init__(self,nodedata):
        self.data=nodedata
        

class linklist:
    first=None
    current=None
    size=0
    def __init__(self,newNode=None):
        if newNode!=None:
            self.first=newNode
            self.current=newNode
            self.size=1
        else:
            print 'u have init a empty linklist'
    
    def insert(self,newNode):
        insertNode=Node(newNode)
        if self.first==None:
            self.first=insertNode
            self.current=insertNode
            self.size+=1
            print 'add a newNode in the first position'
        else:
            self.current.next=insertNode
            self.current=insertNode
            self.size+=1
            print 'add a newNode at the end '


    def getAll(self):
         iterNode=self.first
         for x in range(0,self.size):
             if(iterNode!=None):
                 print 'data:',iterNode.data
                 iterNode=iterNode.next
    

    def reverseByIter(self):
        first=self.first
        reverse=None
        while(first!=None):
            second=first.next
            first.next=reverse
            reverse=first
            first=second
        
        self.first=reverse


    def reverseByRecur(self,first):
        if first.next==None:
            return first
        if first==None:
            return None
        second=first.next
        rest=self.reverseByRecur(second)
        second.next=first
        first.next=None
        return rest

la=linklist()
la.insert('abc')
la.insert('123')
la.insert('777777')
la.insert('12345')
print '1st get all'
la.getAll()
# sort algorithms rdy
la.reverseByIter()
print '2nd get all (reverseByIter)'
la.getAll()
la.first=la.reverseByRecur(la.first)
print '3rd get all (reverseByRecur)'
la.getAll()
