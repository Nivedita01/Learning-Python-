def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
    return True
    
x = int(input("Enter a positive integer: "))
y = is_prime(x)
if y == True:
    print "Prime"
else:
    print "Not Prime"