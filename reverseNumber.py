reverse = 0

def reverse_number_using_loop(number):
    global reverse
    while(number > 0):
        temp = number % 10
        reverse = reverse * 10 + temp
        number /= 10
    return reverse      

number = raw_input("Enter a number: ")
reversed_number = reverse_number_using_loop(int(number))
print "Using loop: %d" %reversed_number

