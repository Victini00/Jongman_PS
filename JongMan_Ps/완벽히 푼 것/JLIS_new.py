A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = [-1] + A
B = [-1] + B
a_len = len(A)
b_len = len(B)

cache = [[-1]*b_len for _ in range(a_len)]

# 두 수열의 길이는 최소 1이라고 생각한다.
def jlis(a,b):

    # variables
    # (-1) 2개를 무조건 먹고 들어간다고 생각하자.
    max_len = 2

    # base case
    # if a==(a_len-1) and b==(b_len-1):
    #    if A[-1]==B[-1]:
    #        return 1
    #    else:
    #        return 2

    # main case
    standard = max([A[a],B[b]])

    # 일단 A 먼저 둘러보자.
    for i in range(a+1,a_len):
        if A[i] > standard:
            if cache[i][b] == -1:
                cache[i][b] = jlis(i,b)
            max_len = max([max_len, 1 + cache[i][b]])

    # 그리고 B.
    for j in range(b+1, b_len):
        if B[j] > standard:
            if cache[a][j] == -1:
                cache[a][j] = jlis(a,j)
            max_len = max([max_len, 1 + cache[a][j]])

    return max_len


# -1 2개는 빼고 생각해야 대니까...
print(jlis(0,0)-2)
