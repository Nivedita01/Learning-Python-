guess_word = "hello"
guess = ""
out_of_attempts = False
guess_count = 0
guess_limit = 3

#checking if user entered word is equal to actual word and is not out of guesses number
while(guess != guess_word and not(out_of_attempts)):
#checking if guess count is less than guess limit
     if(guess_count < guess_limit): 
        guess = raw_input("Enter guess word: ")
        guess_count += 1
     else:
        out_of_attempts = True

if out_of_attempts:
            print "Sorry! You couldn't guess"
else:
            print "You win!"

