import random
print("ROCK-PAPER-SCISSOR GAME")
while True:
    print("enter your choice\n1-Rock\n2-paper\n3-scissor")
    
    choice=int(input("enter your choice"))

    while(choice>3 or choice<1):
        choice=int(input("plese enter the valid choice....."))
    
    
    if(choice==1):
        choice_name='rock'
    elif(choice==2):
        choice_name='paper'
    else:
        choice_name='scissor'

    print("user choice is->",choice_name) 

    print("now its computer's turn!")  

    comp_choice=random.randint(1,3)

    if(comp_choice==1):
        comp_choice_name='rock'
    elif(comp_choice==2):
        comp_choice_name='paper'
    else:
        comp_choice_name='scissor'

    print("computer choice is->",comp_choice_name)

    print("now user choice vs computer choice")

    if(choice==comp_choice):
        result='DRAW'
    elif(choice==1 and comp_choice==2) or(choice==2 and comp_choice==1):
        result='paper'
    elif(choice==1 and comp_choice==3) or (choice==3 and comp_choice==1):
        result='rock'
    elif(choice==2 and comp_choice==3) or (choice==3 and comp_choice==2):
        result='scissor'
    
    if(result=='DRAW'):
        print("<------game is tie!---->")
    elif(result==choice_name):
        print("<----user wins!---->")
    else:
        print("<----computer wins!---->")







