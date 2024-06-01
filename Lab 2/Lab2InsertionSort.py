#Syed Yasoob Ali
#500953533
#2020/09/29

#Lab 2, Insertion Sort

#Will use insertion sort and output the list in descending order (capitals first)
def insertionSort(thelist):
    #Cycles from the start until the end of the thelist
    for i in range(1,len(thelist)):
        pos = thelist[i]

        j = i-1

        #Anything that is less than the current value of 'pos' will be moved ahead
        while j >= 0 and pos > thelist[j]:
            thelist[j+1] = thelist[j]
            j -= 1

        thelist[j+1] = pos
    return thelist

thelist = ['a','A','c','d','C','e','F','h','L','z']
insertionSort(thelist)
print(thelist)
