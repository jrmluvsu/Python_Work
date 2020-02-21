import random
num=random.randint(1,100)
find=0
count=0
while(find!=num):
    find=int(input("Guess a number: "))
    count+=1
    if find==num:
        print(f"You guessed Right in {count} times.")
        break
    else:
        if find<num:
            print("You guessed low.")
        else:
            print("You guessed high.")
    print("Guess Again")
        
