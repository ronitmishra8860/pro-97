print("Welcome to number guessing game!")
number=int("7")
def ques():
     global userInp
     userInp=input("Enter your guess: ")
def ans():
    if(int(userInp)>number):
        print("the number is too greater please guess lesser")
        ques()
        ans()
    if(int(userInp)<number):
        print("the number is too lesser please guess greater")
        ques()
        ans()
    else:
        print("congratulations you won !")    

ques()
ans()        
