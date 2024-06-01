#Syed Yasoob Ali
#500953533

#Lab 1, Question 1

#original array
array1 = [9, 13, 21, 4, 11, 7, 1, 3]

#Find out halfway point of the array by taking it's length and dividing by 2
#Then, add : to the beginning and end of that halfway point in order to seperate the array into the 2 halves
arraySize = len(array1)//2

#Create new array by first taking second half and adding that to the start
array2 = array1[arraySize:] + array1[:arraySize]


#Print rearranged array and averages to both halves
print('Rearranged array is ',array2)

print('First half average is ',sum(array2[:arraySize])/arraySize)

print('Second half average is ',sum(array2[arraySize:])/arraySize)


