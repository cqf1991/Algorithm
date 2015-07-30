class bubbleSort:
    def sort(self,list):
        x=0
        for i in range(len(list)):        
            for j in range(i+1,len(list)):
                if list[j]<list[i]:
                    tmp=list[j]
                    list[j]=list[i]
                    list[i]=tmp                
        return list
       
alist=[4,2,3,5]
IS=bubbleSort()
print IS.sort(alist)
