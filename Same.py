N = int(input())

while N > 1:
    if N % 2 == 0:
        N //= 2
    elif N % 3 == 0:
        N //= 3
    else:
        print("No")
        break

if N == 1:
    print("Yes")
