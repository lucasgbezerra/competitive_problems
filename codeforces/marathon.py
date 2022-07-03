num  = int(input())

while num > 0:
    a, b, c, d = map(int ,input().split())
    participants = 0
    if b > a:
        participants+=1
    if c > a:
        participants+=1
    if d > a:
        participants+=1
    num -= 1
    print(participants)