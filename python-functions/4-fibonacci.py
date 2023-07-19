def fibonacci_sequence(n):
    if n<= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_sequence(n-1)+fibonacci_sequence(n-2)
 
print(fibonacci_sequence(5))