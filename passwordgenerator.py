import string
import random

length=int(input("enter the length of password"))
print("choose the character set for password\ndigits\nletters\npunctuation\nexit")

characterlist=""
while True:
    choice=int(input("pick a number"))

    if(choice==1):
      characterlist+=string.digits
    elif(choice==2):
      characterlist+=string.ascii_letters
    elif(choice==3):
       characterlist+=string.punctuation
    elif(choice==4):
       break
    else:
       print("please pick valid choice")
    
    password=[]

    for i in range(length):
       randomchar=random.choice(characterlist)

       password.append(randomchar)
       print("the random password is"+"".join(password))





