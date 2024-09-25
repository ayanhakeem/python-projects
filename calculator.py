number1=float(input("enter the number1="))
number2=float(input("enter the number2="))
operator=input("enter the operator=")
if(operator=="+"):
    print("summation of these numbers=",number1+number2)

elif(operator=="-"):
    print("subtraction of these numbers=",number1-number2)

elif(operator=="*"):
    print("multipication of these numbers=",number1*number2)

elif(operator=="/"):
    print("division of these numbers=",number1/number2)

elif(operator=="%"):
    print("modulus of these numbers=",number1%number2)

else:
    print("enter valid operator and try again!")



