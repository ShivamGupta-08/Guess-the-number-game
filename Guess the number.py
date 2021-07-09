num = int(18)
guess = int(9)
number = int(0)
left = int(10)
print("Guess The Number!")
print("You Have",guess,"guesses")
print("START!!!!")
while(True):
    number+=1
    left -= 1
    print( "Guess no.",number)
    print(left, "chance/s left")
    int1 = int(input())

    if int1==num:
        print("You won!!")
        print("You won in",number,"move/s")
        print("--------------------|| YOU WON ||--------------------")
        break
    elif number==guess:
        print("You are out of moves!")
        print("--------------------|| YOU LOSE ||--------------------")
        break
    elif int1 == 17 or int1 == 19:
        print("You are close!")
        print("----------------------------------------")
    elif int1>= 20 and int1 <=25:
        print("You have passed the number little bit!")
        print("----------------------------------------")
    elif int1 <= 12 and int1 >= 14 :
        print("You are too much far away!")
        print("----------------------------------------")
    elif int1>num:
        print("You have passed the many numbers !")
        print("----------------------------------------")
    elif int1<num:
        print("You are some numbers far away!")
        print("----------------------------------------")
    else:print("None")
