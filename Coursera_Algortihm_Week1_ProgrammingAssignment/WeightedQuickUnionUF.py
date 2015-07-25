

class WeightedQuickUnionUF:
    count=0
    parent=[] #id[i]
    size=[]   #size[i]
    def __init__(self,N=0):
        self.count=N
        self.parent=[ i for i in range(N)]  # init list [0,1,2,3...]
        self.size=[ 1 for i in range(N)]       

    def validate(self,P):
        if(P<0 or P>self.count):
            print 'validate failed'
            return False
        return True

    def find(self,p):
        if self.validate(p):
            while(p!=self.parent[p]):#!!!
                p=self.parent[p]
            return p
    
    def connected(self,p,q):
        return self.find(p)==self.find(q)

    def union(self,p,q):
        rootP=self.find(p)
        rootQ=self.find(q)
        if(rootP==rootQ):
            return
        if self.size[rootP]<self.size[rootQ]:
            self.parent[rootP]=rootQ
            self.size[rootP]+=self.size[rootQ]
        else:
            self.parent[rootQ]=rootP
            self.size[rootP]+=self.size[rootQ]
      



'''
xb=WeightedQuickUnionUF(10)
xb.union(4,3)
xb.union(3,8)
xb.union(6,5)
xb.union(9,4)
xb.union(2,1)
xb.union(5,0)
xb.union(7,2)
xb.union(6,1)
xb.union(7,3)
print xb.parent   
print xb.size
print xb.connected(3,5)
'''