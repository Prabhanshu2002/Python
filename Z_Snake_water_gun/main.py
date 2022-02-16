import random



def game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='g':
            return True
        elif you=='w':
            return False

    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True

    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("Computer has Choosen\n Snake for s\n Water for w\n Gun for g?")
you = input("It's Your Turn -> ")

randNo = random.randint(1,3)

if randNo==1:
    comp ='s'
elif randNo==2:
    comp = 'w'
elif randNo==3:
    comp = 'g'

print(f"Computer Choose {comp} and You Choose {you} So")
result = game(comp,you)

if  result== None:
    print("Your game has been Tie! ")
elif result :
    print("You Have Won this Game!")
else:
    print("You Lose!")