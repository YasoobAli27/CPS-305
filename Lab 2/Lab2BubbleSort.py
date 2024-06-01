#Syed Yasoob Ali
#500953533
#2020/09/29

#Lab 2, Bubble Sort

#Will use bubble sort and output the list in descending order (capitals first)
def bubbleSort(thelist):
    #Cycles through the list to pass through and compare each element with eachother
    for i in range(len(thelist)-1):
        for j in range(len(thelist)-i-1):
            #Will swap the 2 elements that are being compared if the current one is smaller than the next one
            if thelist[j] < thelist[j+1]:
                temp = thelist[j]
                thelist[j] = thelist[j+1]
                thelist[j+1] = temp
    #Returns the sorted list
    return thelist


thelist = ['a','A','c','d','C','e','F','h','L','z']
bubbleSort(thelist)
print(thelist)
