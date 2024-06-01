#Syed Yasoob Ali
#500953533
#2020/09/29

#Lab 2, Selection Sort

#Will use selection sort and output the list in descending order (capitals first)
def selectionSort(theList):
    #Cycles through the list
    for i in range(len(theList)):

        #Searches for the current lowest value to put at the front of the list
        min_idx = i
        for j in range(i+1, len(theList)):
            if theList[min_idx] < theList[j]:
                min_idx = j
        #Swaps the current lowest value to the front-most of the list
        theList[i], theList[min_idx] = theList[min_idx],theList[i]
        #Cycle repeats until the entire list is ordered in descending order

    return theList

theList = ['a','A','c','d','C','e','F','h','L','z']
selectionSort(theList)
print(theList)

            
