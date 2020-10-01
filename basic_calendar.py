import calendar  
# Enter the month and year  
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
  
# display the calendar  

if((yy >= 1 and yy <= 9999) and ( mm >= 1 and mm <= 12)):
    print(calendar.month(yy,mm))  
elif((yy < 1 or yy > 9999) and (mm < 1 or mm > 12)):      
    print "Enter valid year and month"
elif(yy < 1 or yy > 9999):
    print "Enter valid year"
elif(mm < 1 or mm > 12):
    print "Enter valid month"
  
