import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    command = input().split()
    
    if len(command) > 1:
        stack.append(int(command[-1]))
    elif int(command[0]) == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif int(command[0]) == 3:
        print(len(stack))
    elif int(command[0]) == 4:
        print(1) if len(stack) == 0 else print(0)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)