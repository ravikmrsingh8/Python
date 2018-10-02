import random
print("""
    I am Thinking of a number between 1 and 100.
    Can You Guess?
""")

attempt = 1
gen_num = random.randint(0, 100)
won = False
while attempt <= 6:
    attempt += 1
    num = int(input("your guess?"))
    if num == gen_num:
        print("You rock!!")
        won = True
        break
    elif num < gen_num:
        print("Higher")
    else:
        print("Lower")
if not won:
    print("No more attempts allowed")


