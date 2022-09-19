# -------입력-------------
A = list(map(int, input().split()))
B = list(map(int, input().split()))
len_a = len(A)
len_b = len(B)

# 왜 +1이 들어가는가?
# 하나의 순열(A 또는 B)가 맨 뒤까지 가서 빈칸인 경우 생각.
cache = [[-1]*(len_b+1) for _ in range(len_a+1)]


# main func.

def jlis(a,b):
    # 인자로 받는 것은, A와 B의 시작 인덱스이다.
    # 반환값은 최대 '길이'
    returnlen = 0
    # base case
    if a==len_a and b==len_b:
        return 0

    # main case
    # A의 첫번째 선택
    for i in range(a,len_a):
        check = A[a]
        if check<A[i]:
            # memoization 확인
            if cache[i][b] != -1:
                returnlen = max([returnlen,1 + cache(i,b)])
            else:
                cache[i][b] = jlis(i,b)
                returnlen = max([returnlen,1 + cache(i,b)])

        for j in range(b,len_b):
            if check<B[j]:
               # memoization 확인
                if cache[a+1][j] != -1:
                    returnlen = max([returnlen,1 + cache(i,b)])
                else:
                    cache[i][b] = jlis(i,b)
                    returnlen = max([returnlen,1 + cache(i,b)])
 


    # B의 첫번째 선택



    
    
    


        


    
    
















# ------testcase----------