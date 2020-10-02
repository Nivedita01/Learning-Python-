def expo_number(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
    
base_number = int(input("Enter base number: "))
exponent = int(input("Enter exponent: "))
print expo_number(base_number,exponent)