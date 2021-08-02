for _ in range(int(input())):
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    c = a & b
    if c:
        print('YES')
        print(1, c.pop())
    else:
        print('NO')
