import WeightedQuickUnionUF
class Percolation:
    count=0
    WQUF=None
    sideN=0
    isOpen=[]
    def __init__(self,N):
        self.count=N*N
        self.sideN=N
        self.WQUF=WeightedQuickUnionUF.WeightedQuickUnionUF(N*N+2)
        self.isOpen=[ False for i in range(N*N+1)] #give up isOpen[0]
        self.isOpen[0]=0
        for i in range(1,N+1):
            self.WQUF.union(0,i)
        for i in range(N*N,N*N-N,-1):
            self.WQUF.union(N*N+1,i)

        

    def open(self,i,j):
        self.validate(i)
        self.validate(j)
        subX=i-1   # column i & j  -> subscript
        subY=j-1
        nowPosition=subX*self.sideN+j
        if self.isOpen[nowPosition] is False:
            self.isOpen[nowPosition]=True
            if i>1 and self.isOpen[nowPosition-self.sideN] is True:
                self.WQUF.union(nowPosition-self.sideN,nowPosition)
            if i<self.sideN  and self.isOpen[nowPosition+self.sideN] is True:
                self.WQUF.union(nowPosition+self.sideN,nowPosition)
            if j>1 and self.isOpen[nowPosition-1] is True:
                self.WQUF.union(nowPosition-1,nowPosition)
            if j<self.sideN and self.isOpen[nowPosition+1] is True:
                self.WQUF.union(nowPosition+1,nowPosition)



    def validate(self,P):
        if(P<1 or P>self.sideN):
            print 'validate failed'
            return False
        return True


    def isOpen(self,i,j):
        if self.validate(i) and self.validate(j):
            return self.isOpen[(i-1)*self.sideN+j]

      
    def isFull(self,i,j):
        if self.validate(i) and self.validate(j) and self.isOpen(i,j):
            return self.WQUF.connected(0,(i-1)*self.sideN+j)


    def percolates(self):
        return self.WQUF.connected(0,self.sideN*self.sideN+1)


pe=Percolation(5)
print pe.WQUF.parent
pe.open(2,3)
pe.open(3,2)
pe.open(3,4)
pe.open(4,3)
pe.open(3,3)
pe.open(1,3)
pe.open(4,4)
pe.open(5,5)
print pe.isOpen
print pe.WQUF.parent
print pe.percolates()