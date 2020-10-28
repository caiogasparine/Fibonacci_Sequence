if __name__ == '__main__':
    n = int(input("How many numbers do you want to display? "))
    n1, n2 = 0, 1
    count = 0
    # check if the number of values is > 0
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci Sequence ", n, ":")
        print(n1)
    else:
        print("Fibonacci Sequence Results:")
        while count < n:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
