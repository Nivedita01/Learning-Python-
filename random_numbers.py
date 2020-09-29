from random import random, sample

#random floating-point number 
num = random()
print "Random float 0.0 - 1.0: ", num

#cast floating point random number to integer
rnum = int(num * 10)
print "Random float 0 - 10: ", rnum

#add multiple random integers to a list
rnums =[]; i =0
while(i<6):
    rnums.append(int(random() * 10) +1)
    i += 1
print "Random multiple integers between 1 - 10: ", rnums

#assign multiple unique random integers to list
urnums = sample(range(1, 99), 5)
print "Random unique integers between 1 - 99: ", urnums



