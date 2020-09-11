import Stack

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    
    # TODO: Intiate stack object
    stack = Stack.Stack()    
    # TODO: Interate through equation checking parentheses
    for equ in equation:
        if equ== "(":
            stack.push("(")
        elif equ == ")":
            if stack.pop() is None:
                return False
        
    # TODO: Return True if balanced and False if not
    return stack.size() == 0

print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/((2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
#print(equation_checker('((3^2 + 8)*(5/2))/(2+6))'))

    
