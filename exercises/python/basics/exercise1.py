num = int(input("Your number is? : "))

fact = 1

if num < 0:
    print("Number needs to be a positive number")
else:
    for i in range(1,num +1):
        fact = fact * i
    print("The factorial of ", num, "is ", fact)
