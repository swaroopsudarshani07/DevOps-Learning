
def sum_even(N):
    total = 0
    for i in range(2, N + 1, 2):
        total += i
    print("Sum of even numbers =", total)

num = int(input("Enter N: "))
sum_even(num)