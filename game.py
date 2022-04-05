import random

name = input("Hello! What's your name?\n")


print("Hello ", name, ".", " I'm thinking of a number between 1 and 100. Try to guess it!", sep='')

num = random.randint(0, 100)

guess = None
tries = 1

while guess != num:
    guess = int(input('Enter Number: '))

  
    if guess == num:
        print('Well done! You guessed the number in', tries, 'tries!')
        break
      
    elif guess > num:
        print(f'{guess} is too high.\n')
        tries += 1
        

    elif guess < num:
        print(f'{guess} is too low.\n')
        tries += 1

    else:
        print('Something went wrong!')
        break