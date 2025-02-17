import sys
input = sys.stdin.readline

dict, s = {}, input()[:-1]

for i in range(97, 97+27):
    dict[chr(i)] = [0 for _ in range(len(s))]

for idx, i in enumerate(s):
    dict[i][idx] += 1
    if idx > 0:
        for j in dict.keys():
            dict[j][idx] += dict[j][idx-1]

for i in range(int(input())):
    c, s, e = map(str, input().split())
    s = dict[c][int(s)-1] if int(s)-1 >= 0 else 0
    print(dict[c][int(e)] - s)