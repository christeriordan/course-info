def fibonacci(number):
    n1,n2 = 0,1
    count = 0
    if number <= 0:
        return print("Please enter a positive integer")
    elif number == 1:
        return print("Fibonacci sequence upto ", number, ":")
    else:
        print("Fibonacci sequence:")
        while count < number:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


fibonacci(-1)
