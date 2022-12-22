def fibonacci(n):
    if n == 1 or n == -1:
        return 1
    elif n == 0:
        return 0
    else:
        if n > 0:
            return fibonacci(n-1) + fibonacci(n-2)
        else:
            return fibonacci(n+2) - fibonacci(n+1)

n = int(input('Введите n: '))
my_list = []

for i in range(-n, n+1):
    my_list.append(fibonacci(i))
print(my_list)