cache = [[-1 for _ in range(1000)] for _ in range(100)]

def pack(N, W):
    if cache[N][W] != -1:
        return cache[N][W]
    
    # base case
    if N == n:
        return 0
    
    # 담지 않을 경우
    ret = pack(N+1, W)
    
    # 담을 경우 : 용량 생각해야 함
    if volume[N] <= W:
        ret = max([ret, pack(N+1, W-volume[N]) + score[N]])
        
    cache[N][W] = ret
    return ret

#---------------------------------------

name = []
volume = []
score = []
answer = []

n, w = map(int, input().split())

for i in range(n):
    nam, vol, sco = input().split()
    
    name.append(nam)
    volume.append(int(vol))
    score.append(int(sco))

pack(0,w)
print(cache[0][w])
# ----------------------
    
mem_W = 0
    
for i in range(n-1):
    if cache[i][w-mem_W] == cache[i+1][w-mem_W]:
        # 안고르는 경우
        pass
    else:
        mem_W += volume[i]
        answer.append(name[i])
        
#-----------
for i in answer:
    print(i)
    
    
'''
6 10
laptop 4 7
camera 2 10
xbox 6 6
grinder 4 7
dumbell 2 5
encyclopedia 10 4

6 17
laptop 4 7
camera 2 10
xbox 6 6
grinder 4 7
dumbell 2 5
encyclopedia 10 4

'''
