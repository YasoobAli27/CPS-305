#Syed Yasoob Ali
#500953533
#Lab 4

#Question 3
#Found assistance for solution on GeeksforGeeks with code from Ankitrai01 & Raju Pitta

#Will create a stack with each element of the expression being pushed into it
def balanceCheck(expr): 
    stack = [] 

    #If the following is a left bracket, it will get pushed into the stack
    for char in expr: 
        if char in ["("]: 
  
            # Push the element in the stack 
            stack.append(char) 
        else: 

            #If it's not a left bracket, then it must be a right one
            if not stack: 
                return False
            current_char = stack.pop() 
            if current_char == '(': 
                if char != ")": 
                    return False
  
    #Checks to see if stack is empty.
    #If it is empty, then that means that it is not balanced
    if stack: 
        return False
    #Otherwise, it will return true
    return True


#Input to test  
if __name__ == "__main__": 
    expr = "(())"
      
    #outputs if they are balanced or not based on the check
    if balanceCheck(expr): 
        print("The following is balanced") 
    else: 
        print("The following isn't balanced") 
