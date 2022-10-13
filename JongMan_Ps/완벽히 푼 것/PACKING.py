# 얘는 최대점수 저장 버전.. 

# 이걸로 풀 수 있다.

# 이걸로 최대는 구할 수 있는데... 선택 기록 함수 어카지..
# 물건의 수는 N(1부터 100)
# 캐리어의 용량은 W(1부터 1000)

cache = [[-1 for _ in range(1000)] for _ in range(100)]

# item_num '이상'의 item부터 선택 가능하다
# left_weight는 이제 남은 용량.
# score는 절박도

# 중요! pack의 정의란?
# 고를 수 있는 번호는 item_num부터, 남은 left_weight는 저만큼일때,
# 그리고 지금까지의 점수가 score일 때, 나올 수 있는 맥스 점수.

# 더 중요! 그럼 cache에는 어케 저장하는가?
# 2차원배열인데 그럼 score 정보는 버리는가?
# max 함수를 이용해서 그 조건상에서 나올 수 있는 최대 점수 저장.
def pack(item_num, left_weight, score):
    # base case
    # 0. memoization
    if cache[item_num][left_weight] != -1:
        return cache[item_num][left_weight]
    
    # 1. item number가 끝에 도착한 경우	
    if item_num == N:
        cache[N][left_weight] = max([score, cache[N][left_weight]])
        return cache[N][left_weight]
    
    # 여기서 경우 나누는 실수
    # 2. item_num은 범위에 들어와서 괜찮은데, 못 고르는 경우.
    if item_list[item_num][1] > left_weight:
        cache[item_num][left_weight] = max([score, cache[item_num][left_weight]])
        return cache[item_num][left_weight]
        
    
    # 선택하는 경우, 선택하지 않는 경우
    select_yes = pack(item_num+1, left_weight-item_list[item_num][1], score+item_list[item_num][2])
    select_no = pack(item_num+1, left_weight, score)
    
    cache[item_num][left_weight] = max([select_no, select_yes, cache[item_num][left_weight]])
    return cache[item_num][left_weight]

# ------------------------------    
N, W = map(int, input().split())

item_list = []

for _ in range(N):
    mem = list(input().split())
    mem[1] = int(mem[1])
    mem[2] = int(mem[2])
    item_list.append(mem)
    
# item_list를 정렬한다.
# 일단, 부피를 기준으로 정렬한다
# 부피가 동일한 경우는, 절박도가 큰 것부터! 앞에 놓는다.

# 정렬을 반드시 해야 하는 경우는, 위의 #2. 경우 때문에 그럼.
item_list.sort(key=lambda x:(x[1],-x[2]))

print(pack(0,W,0))


# -------------------------------
mem_weight = item_list[0][1] # 첫번째 꺼 무게, 나중에는 1개 1개의 무게로 memoization 된다.
accumulated_weigth = 0 # 지금까지 고른 놈들의 총 무게.
mem_score = 0 # 딱히 필요없긴 함.. 얘는 차피 위에서 계산됨
mem_list = []

for i in range(len(item_list)):
    
    # 뒤에 +가 엎으면 당연히 select_no가 유리하므로
    # 고른거랑 안고른거 비교하려면 당연히 점수를 더해서 생각해줘야 함.
    # select_yes = cache[i+1][W-mem_weight-accumulated_weigth] + mem_score + item_list[i][2] 
    # select_no = cache[i+1][W-accumulated_weigth] + mem_score
    
    
    if cache[i][W-accumulated_weigth] == cache[i+1][W-accumulated_weigth-item_list[i][1]] and item_list[i][1] <= W-accumulated_weigth:
        print("select! " + str(i), str(W-accumulated_weigth), str(cache[i][W-accumulated_weigth]))
        mem_score += item_list[i][2]
        # 여기 더 못넣어서 끝난 경우 append(0)하는 조건문 추가
        mem_list.append(1)
        accumulated_weigth += mem_weight
        #indexerror 보정
        if i != len(item_list) -1:
        	mem_weight = item_list[i+1][1]
        
    else:
        print("no select " + str(i), str(W-accumulated_weigth), str(cache[i][W-accumulated_weigth]), str(cache[i+1][W-accumulated_weigth-item_list[i][1]]))
        mem_list.append(0)
        if i != len(item_list) -1:
        	mem_weight = item_list[i+1][1]
        
for i in range(len(mem_list)):
    if mem_list[i] == 1:
        print(item_list[i][0])
    else:
    	pass
        
print(mem_list)

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
    
