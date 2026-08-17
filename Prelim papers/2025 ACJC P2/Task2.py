#Task 2.1
def quicksort(lis):
    if len(lis) <= 1:
        return lis
    low = 0
    high = len(lis) 
    mid = (low + high) // 2
    pivot = lis[mid]
    rest = lis[:mid] + lis[mid+1:]
    
    smaller = [value for value in rest if value < pivot]
    larger = [value for value in rest if value >= pivot]
    
    return quicksort(smaller) + [pivot] + quicksort(larger)

lis = [3,2,9,0,4,17,8]
print(quicksort(lis))

def insertionsort(lis):
    for i in range(1 , len(lis)):
        cur = lis[i]
        pos = i - 1
        while pos >= 0 and lis[pos] > cur:
            lis[pos+1] = lis[pos]
            pos -= 1
            
        lis[pos+1] = cur
        
    return lis

print(insertionsort(lis))

#Task 2.2
import timeit 
import random
setup_code = "from __main__ import quicksort, lis1" 
time = timeit.timeit("quicksort(lis1)", setup_code, number=1) 
print(time)


for i in range(1000):
    lis1.append(i)
    
for j in range(1000):
    lis2.append(j)
    
for 
    

