# n은 개수, k는 맨 위칸의 블럭 개수

n=int(input())

#poly_piece의 cache.
cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]

def Poly_piece(n, k):
    if n==k:
        return 1
    ret = 0
    for i in range(n-k):
        if cache[n-k][i+1] == -1:
            cache[n-k][i+1] = Poly_piece(n-k, i+1)
        ret += cache[n-k][i+1] * (i+k)

    return ret

def Poly(n):
    sum = 0
    for i in range(n):
        if cache[n][i+1] == -1:
            cache[n][i+1] = Poly_piece(n, i+1)
        sum += cache[n][i+1]

    return sum

#--------------------------
print(Poly(n)%10000000)