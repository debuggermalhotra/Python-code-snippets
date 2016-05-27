def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                
s = raw_input("ENTER THE NUMBERS TO BE SORTED: ")
numbers = map(int, s.split())
bubbleSort(numbers)
print(numbers)
