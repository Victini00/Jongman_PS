n = int(input())
cache_sym = [1,1,2]+[-1 for _ in range(n-2)]

def sym(n):
    if n == 1 or n == 2:
        return n

    if cache_sym[n] != -1:
        return cache_sym[n]

    for i in range(1,3):
        if cache_sym[n-i] == -1:
            cache_sym[n-i] = sym(n-i)
    
    return cache_sym[n-1] + cache_sym[n-2]

    
def Q(n):
    if n == 1 or n == 2:
        return 0
    
    for i in range(3):
        if cache_sym[int((n/2)-i)] == -1:
            cache_sym[int((n/2)-i)] = sym(int((n/2)-i))
        
    if n%2 == 0:
        return sym(n) - cache_sym[int((n-2)/2)] - cache_sym[int(n/2)]
    else:
        return sym(n) - cache_sym[int((n-1)/2)]

print(Q(n)%1000000007)