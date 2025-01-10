#Random Fibonaccie Generator

def generate_fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Series:", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Input
n = int(input("Enter the number of terms in the Fibonacci series: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    generate_fibonacci(n)
