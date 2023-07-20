def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        if next_number < 0:
            return []  # incorrect input
        fibonacci_numbers.append(next_number)

    return fibonacci_numbers[:n]

n = 10
result = fibonacci_sequence(n)
print(result)
 
print(fibonacci_sequence(5))