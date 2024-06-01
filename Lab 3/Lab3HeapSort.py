#Syed Yasoob Ali
#500953533
#2020.10.6

#Lab 3, Heap Sort

#Sources:
#Received help from one of my friends at Wilfred Laurier Computer Science


#Heap sort will find the maximum element and place it at the end
#Will repeat until the entire array is sorted
#Since we are sorting in descending order, the maximum element will get placed at the beginning

def heapify(List, i, N):
    small = i
    left = i * 2 + 1
    right = i * 2 + 2

#Based on what is smaller, small will be assigned to either the left or right end
    if (left < N and List[small] > List[left]):
        small = left

    if (right < N and List[small] > List[right]):
        small = right

#If the smallest element is not i, it will swap them
    if (small != i):
        List[small], List[i] = List[i], List[small]

#Runs the subprogram again
        heapify(List, small, N)

#Will run heapify until the list has been sorted
def heapSort(List):
    N = len(List)

    for i in range(N//2 - 1, -1, -1):
        heapify(List, i, N)

    for i in range(N-1, 0, -1):
        List[i], List[0] = List[0], List[i]
        heapify(List, 0, i)

#Creates list, runs the subprogram and prints the list
List = ['F', 'a', 'c', 'e', 'z', 'A', 'y', 'X', 'B']
print(List)
heapSort(List)
print(List) 
