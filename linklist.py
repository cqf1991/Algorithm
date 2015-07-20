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
             print 'data:',iterNode.data
             iterNode=iterNode.next
    
la=linklist()
la.insert('abc')
la.insert('123')
la.insert('777777')
la.insert('12345')
la.getAll()

