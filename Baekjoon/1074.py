n, r, c = map(int, input().split())

def find_quadrant(n, r, c, ans=0):
    if n == 0:
        print(ans)
    else:
        std = 2**(n-1)
        tmp = (n - 1) * 2

        # 2사분면
        if r < std and c < std:
            return find_quadrant(n-1, r, c, ans+0)
        # 1사분면
        elif r < std and c >= std:
            return find_quadrant(n-1, r, c-std, ans+2**(tmp))
        # 3사분면
        elif r >= std and c < std:
            return find_quadrant(n-1, r-std, c, ans+((2**(tmp))*2))
        # 4사분면
        else:
            return find_quadrant(n-1, r-std, c-std, ans+((2**(tmp))*3))

find_quadrant(n, r, c)