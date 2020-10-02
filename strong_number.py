sum = 0
number = int(input("Enter an integer: ")) 
temp_number = number                                         
while(number > 0):                                   
    i = fact = 1
    rem = number%10                                
    #finding factorial 
    while(i <= rem):                                    
        fact = fact * i                                    
        i = i + 1                                              
    sum += fact                                           
    number = number//10                           
if(sum == temp_number):
    print "It is a strong number"
else:
    print "It is not a strong number"

    
    
    
