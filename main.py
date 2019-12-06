# чтение списка
def read(L):
    for elem in L:
        print(elem)

# сумма элементов списка
def sum(L):
    result = 0
    for elem in L:
        result += elem
    return result

# поиск наибольшего элемента в списке
def find_max(L):
    max_elem = L[0]
    for i in range(1,len(L)):
        if L[i] > max_elem:
            max_elem = L[i]
    return max_elem

#  максимум из четных
def find_max_even(L):
    max_even_elem = -1
    for elem in L:
        if elem % 2 == 0 and elem > max_even_elem:
            max_even_elem = elem
    return max_even_elem

# два максимума
def find_two_max_elems(L):
    max_1 = L[0]
    max_2 = L[1]
    
    # упорядочиваем
    if max_2 > max_1:
        max_1, max_2 = max_2, max_1
    
    for i in range(2,len(L)):
        if L[i] > max_1:
            max_1, max_2 = L[i], max_1
        
        elif L[i] > max_2:
            max_2 = L[i]
    
    return (max_1, max_2)

# простое ли число
def is_simple_number(x):
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True

# факториал
def factorize(x):
    result = 1
    for i in range(2,x+1):
        result *= i
    return result

# рекурсивный факториал
def factorize_recursive(x):
    if x == 0:
        return 1
    return x * factorize_recursive(x-1)

# разложить число на множители
def factor_number(x):
    divisors = []
    divisor = 2
    while x >= divisor:
        while x % divisor == 0:
            divisors.append(divisor)
            x //= divisor
        divisor += 1
    return divisors

# копирование массива
def copy_list(L):
    # return list(L)
    copy = []
    for elem in L:
        copy.append(elem)
    return copy

# копирование в обратном порядке
def reverse_copy(L):
    # return list(reversed(L))
    copy = []
    for i in range(len(L)-1, -1, -1):
        copy.append(L[i])
    return copy

# бинарный поиск в списке
def left_bound(L,key):
    left = -1
    right = len(L)
    while right - left > 1:
        middle = (left + right)//2
        if  L[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_bound(L,key):
    left = -1
    right = len(L)
    while right - left > 1:
        middle = (left + right)//2
        if  L[middle] <= key:
            left = middle
        else:
            right = middle
    return right

def binary_search(L,key):
    l = left_bound(L, key)
    r = right_bound(L, key)
    print(f'There is {r - l - 1} keys in list',end=' ')
    if r - l > 1: 
        print(f'starts from index {l + 1} to {r - 1}')

# число фиббоначи
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_dynamic(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n-1]

#  создание двумерного массива
def create_table(height, width):
    return [[0]*width for i in range(height)]

my_table = create_table(2,9 )
# print(my_table)

t = [[0]*10 for i in range(2)]
print(t)
