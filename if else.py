#check if alegible to vote
age=int(input("enter your age") )
if age>=18:
    print("you are alegible to vote")
else:
    print("you are not alegible to vote")

#check if number is even or odd
num=int(input("enter a number"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")
    ##good morning program
    hour=int(input("enter the hr in 24 hr format"))
    if hour<12:
        print("good morning")
    else:
        print("good afternoon")