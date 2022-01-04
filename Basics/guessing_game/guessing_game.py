secret = "giraffe"
guess = ""
guess_count = 0
max_guesses = 3
out_of_guesses = False

while guess != secret and not(out_of_guesses):
    if guess_count < max_guesses:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
    
if out_of_guesses:
    print("uh oh!")
else:
    print("You got it")


