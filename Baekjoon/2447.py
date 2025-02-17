def star(n):
    if n == 1:
        return ['*']
    
    S = star(n//3)
    
    L = []
    for i in S:
        L.append(i * 3)
    for i in S:
        L.append(i + ' '*(n//3) + i)
    for i in S:
        L.append(i * 3)

    return L

print(*star(int(input())), sep='\n')