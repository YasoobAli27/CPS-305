#Syed Yasoob Ali
#500953533

#Lab 1, Question 5

#Insert function, assume 0 <= k <= n
def insert(self, k, value):
    if self._n == self.capacity: #not enough room
        largeArray = self._make_array(2*self.capacity) # so double capacity by creating a new larger array

        for j in range(k):
            largeArray[j] = self._A[j]      
        largeArray[k] = value               #cycles through the array and assigns current element to value

        for j in range(k, self._capacity):
            largeArray[j+1] = self._A[j]
            self._capacity = 2 * self._capacity
            self._A = largeArray

    else:
        for j in range(self._n, k, -1)                # shift rightmost first
            self._A[j] = self._A[j-1]

        #stores newest element
        self._A[k] = value

    self._n += 1
