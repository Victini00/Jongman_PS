d,q = int(input().split())

cache = [[-1 for _ in range(101)] for _ in range(51)]

# 연결 여부를 판단하는 행렬
connected = [[0 for _ in range(51)] for _ in range(51)]
# 차수를 기록해둔 행렬
degree = [0 for _ in range(51)]


# search 함수의 정의: days에 here에 숨어있을 때, 마지막 날 q번 마을에 있을 조건부 확률

def search(here, days):
    # base case
    if days == d:
        return 1.0 if here == q else 0.0
    
    # memoization case
    ret = cache[here][days]
    
    if ret > -1: return ret
    
    ret = 0.0
    for there in range(n):
        if connected[here][there]:
            # 연결되어 있는 경우.
            # search 함수의 정의를 잘 생각해보자.
            # here -> there(1회 이동), days -> days + 1(마찬가지로 1회 이동)
            # search(there, days+1)을 알고 있다는 가정 하에, 글로 갈 확률은 1/ deg[here]이다.
            ret += search(there, days+1) / deg[here]
            
    return ret

# serach2 함수의 정의: 비슷하지만, 마지막에서부터 온다.
# cache와 connected, degree는 동일하게 사용함.

def search2(here, days):
    # base case
    # 거꾸로 가기 때문에, days가 0일때가 base case가 된다.
    if days == 0:
        return 1.0 if here == q else 0.0
    
    # memoization case
    ret = cache[here][days]
    
    if ret > -1 return ret

    ret = 0.0
    for there in range(n):
        if connected[here][there]:
            # days가 -1이 되는 거 인지.
            # deg도 here가 아니라 there의 deg를 씀에 주의!!
            ret += search(there, days-1) / deg[there]
            
    return ret
    
            
    
    
    
    
    
