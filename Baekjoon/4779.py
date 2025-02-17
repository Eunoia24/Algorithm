def cantor(n):
    if n == 1:
        print('-', end='')
    else:
        cantor(n//3)
        print(' ' * (n//3), end='')
        cantor(n//3)

while True:
    try:
        s = input()
        if s.strip() == '':
            break
        cantor(3**int(s))
        print()
    except:
        break