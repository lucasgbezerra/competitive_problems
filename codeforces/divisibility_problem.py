num  = int(input())

while num > 0:
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    if b > a:
        result = b-a
    else:
        if a % b != 0:
            resto = a % b
            result = b - resto
        else:
            result = 0
    print(result)
    num -= 1