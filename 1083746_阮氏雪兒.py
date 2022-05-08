from stack_diy import Stack

def iostep(in_cabin, out_cabin):

    #Function to take the top element of the stack    
    def peek_stack(stack):
        if stack.isEmpty() == False:
            return stack.data[stack.top]
        else:
            return None
    
    #Set initial values for variables
    count = 0
    step = []
    cabin = Stack(len(in_cabin))
    in_stack = Stack(len(in_cabin))
    
    #Push the elements in in_cabin in reversed way
    for i in reversed(in_cabin):
        in_stack.push(i)
    
    #For elements in out_cabin
    for i in out_cabin:
        
        #In case the cabin stack is not empty 
        #and the first element of the cabin is equal to elements in out_cabin 
        if cabin.isEmpty() == False and peek_stack(cabin) == i:
            count+=1
            cabin.pop()
            step.append("pop")
        
        #In case the cabin stack is empty 
        elif in_stack.isEmpty() == True:
            while(cabin.isEmpty() == False):
                step.append("pop")
                if i == cabin.pop():
                    count += 1
                    break
                
        #If not equal, will 'pop' the element out from the stack    
        else:
            while in_stack.isEmpty() == False:
                temp = in_stack.pop()
                cabin.push(temp)
                step.append("push")
                if temp == i:
                    count += 1
                    cabin.pop()
                    step.append("pop")
                    break
                
    #Return the result
    if count == len(out_cabin):
        return step
    return [] #If the process cannot work, return empty list


if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [1,2,3])
    print(step)

#留言板