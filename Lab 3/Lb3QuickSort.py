#Syed Yasoob Ali
#500953533
#2020.10.6

#Lab 3, Quick Sort

#Sources:
#Recieved help from one of my friends at Wilfred Laurier Computer Science


#Quick sort will pick a value (pivot) by using the rightmost on the list.

#Subprogram to create the partition
def partition(List, left, right):
    i = left - 1
    pivot = List[right]

#Cycles through the list, check to see if the current element is higher than the one on the right
    for j in range(left, right):
        if (List[j] > pivot):
            i += 1
            List[i], List[j] = List[j], List[i]

    i += 1
    List[i], List[right] = List[right], List[i]
    return i

#if the left is greater than right, it will adjust the partition
def quick_sort_util(List, left, right):
    if (left < right):
        p = partition(List, left, right)

        quick_sort_util(List, left, p-1)
        quick_sort_util(List, p+1, right)

#Subprogram will check length of list to see if it is above 1
def quick_sort(List):
    N = len(List)

    if (N == 1):
        return
    quick_sort_util(List, 0, N-1)

#Creates list, runs the subprogram and prints the list
List = ['F', 'a', 'c', 'e', 'z', 'A', 'y', 'X', 'B']
print(List)
quick_sort(List)
print(List) 


