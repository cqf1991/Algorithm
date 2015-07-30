class shellSort:
    def sort(self,list):
        N = len(list)
        h = 1
        while(h < N / 3):
            h = 3 * h + 1 #increment sequence 3X+1 1,4,13,40,121.....
        while(h >= 1):
            for i in range(N):
                for j in range(i,0,-h):
                    if list[j] < list[j - h] and j >= h:
                        list[j],list[j - h] = list[j - h],list[j] # part insertion sort
            h = h / 3
        return list


alist = ['S','H','E','L','L','S','O','R','T','E','X','A','M','P','L','E']
ss = shellSort()
print ss.sort(alist)