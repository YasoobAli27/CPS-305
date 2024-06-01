#Syed Yasoob Ali
#500953533

#Lab 1, Question 2

#Array can be replaced with whatever numbers you want
array1 = [1, 4, 14, 2, 1, 3, 5, 6, 23]

#Left side of the array is the beginning, while right side will be the final element
leftSide = 0
rightSide = len(array1) - 1

#Will cycle through the array from the left side. Every time it detects an odd-number, it will be moved to the end of the array
#It does this by swapping it's position with 'right'. After it has swapped a number, right will be moved 1 to the left and the cycle continues
#Eventually, it will reach the end, with all of the odd numbers on the right side, leaving only even numbers on the left side
while (leftSide < rightSide):

    #If the number is divisble by 2, it is even and will be kept in it's current location. Instead, left position will move 1 to the right
    while (array1[leftSide] % 2 == 0 and leftSide < rightSide):
        leftSide += 1
    #If the number is odd, it will be replaced and right will move 1 position left.
    while (array1[rightSide] % 2 == 1 and leftSide < rightSide):
        rightSide -= 1

    #While left is still going up, it will swap the positions of the numbers if required
    if (leftSide < rightSide):
        array1[leftSide], array1[rightSide] = array1[rightSide], array1[leftSide]
        leftSide += 1
        rightSide -= 1

#Prints the finalized array
print('rearranged array is ',array1)
        
