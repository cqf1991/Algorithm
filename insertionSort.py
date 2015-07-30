class insertionSort:
    def sort(self,list):
        for i in range(len(list)):
            for j in range(i,0,-1):
                if list[j] < list[j-1]:
                    list[j-1],list[j] = list[j],list[j-1]#swap list[j] & list[j-1] implement insertion
        return list
alist = [4,3,2,5]
IS = insertionSort()
print IS.sort(alist)