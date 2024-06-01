#Syed Yasoob Ali
#500953533

#Lab1, Question 4

import ctypes          #Provides low-level arrays

class DynamicArray:
    #A dynamic array class akin to a simplified Python list

    def __init__(self):
        #create an empty array
        self._n = 0                                 #count actual elements
        self._capacity = 1                          #default array capacity
        self._A = self._make_array(self._capacity)  #low-level array


    def __len__(self):
        #Return number of elements stored in the array
        return self._n

    def __getitem__(self, k):
        #Return element at index k

        
        if k < 0:
            return self._A[(self._n + k)            #if k is negative, will return self._A but will also add k to self._n in order to support negative indices
        
        if not 0 <= k < self._n:
            raise indexError('invalid index')
        return self._A[k]                           #retrieve from array

    def append(self, obj):
        #Add object to the end of the array
        if self._n == self._capacity:               #not enough room
            self._resize(2 * self._capacity)        #doubles capacity
            self._A[self._n] = obj
            self._n += 1

    def _resize(self, c):                           #nonpublic utlity
        #resize internal array to capacity c
        B = self._make_array(c)                     #new bigger array
        for k in range(self._n):                    #for each existing value
            B[k] = self._A[k]

        self._A = B                                 #use the bigger array
        self._capacity = c

    def _make_array(self, c):                       #nonpublic utlity
        #Return new array with capacity c

        return (c * ctypes.py_object)()             #see ctypes documentation
    
        

        
