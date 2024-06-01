#Syed Yasoob Ali
#500953533

#Lab1, Question 3

#Kept almost all the lines from the original code the same except for n, which I decided to replace with 30
import sys

data = []

#new variable to keep track of which one it is currently on
current = 0

for k in range(30):
    a = len(data)
    b = sys.getsizeof(data)

    #if the size is larger than the current number and is still in range, it will replace b to become the new highest and will print it
    if b > current and a > 0:
        current = b
        print('Capacity exausted at length:', a - 1)
        
    data.append(None)
