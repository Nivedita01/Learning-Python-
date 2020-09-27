def swap_with_addsub_operators(x,y):
            # Note: This method does not work with float or strings
            x = x + y
            y = x - y
            x = x - y
            print("After: " +str(x)+ " " +str(y))                          
            
def swap_with_muldiv_operators(x,y):
            # Note: This method does not work with zero as one of the numbers nor with float
            x = x * y
            y = x / y
            x = x / y
            print("After: " +str(x)+ " " +str(y))                          

def swap_with_builtin_method(x,y):
            # Note: This method works for string, float and integers
            x,y = y,x
            print("After: " +x+ " " +y)               


x = raw_input("Enter first input: ")
y = raw_input("Enter second input: ")
print("Before:  " +x+ " " +y) 
swap_with_addsub_operators(int(x), int(y))
swap_with_muldiv_operators(int(x), int(y))
swap_with_builtin_method(x, y)

