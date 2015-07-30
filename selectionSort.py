class selectionSort:
    def sort(self,list):
        for i in range(len(list)):   
            min = i     
            for j in range(i + 1,len(list)):
                if list[j] < list[min]:
                    min = j
            list[min],list[i] = list[i],list[min]   #swap                       
        return list
       
alist = [4,2,3,5]
IS = selectionSort()
print IS.sort(alist)
