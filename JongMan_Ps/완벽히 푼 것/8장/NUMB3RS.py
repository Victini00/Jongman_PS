# 행렬의 결합법칙 이용.

# input 조건에 따라 최대 제곱횟수는 100회이므로,
# 2진법으로 생각했을 때 7자리만 있으면 됨.

# 잘 됨!
# [[1,2],[3,4],[5,6]],[[7],[8]] -> [[23],[53],[83]]
def Matrix_mul(A, B):
    
    ret = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                ret[i][j] += A[i][k] * B[k][j]
                
    return ret

# 얘도 잘 됨.
# 7 -> [0,0,0,0,1,1,1]
def dec_to_bin(n):
    check = len(bin(n)[2:])
    
    ret = [0 for _ in range(7-check)]
    for i in bin(n)[2:]:
        ret.append(int(i))
        
    return ret
    

# 맨 앞쪽 1을 찾아서 거기까지 제곱을 해나가야함.
# 17이면, [0,0,1,0,0,0,1]이므로 1,2,4,8,16까지.
# 맨 앞쪽의 1은, list의 index 함수로 찾을 수 있다.

# near_lst와 d를 넣어주면, cache_mullist를 되돌려준다. 
# ex) 17과 near_lst를 넣어주면, [-1, -1, lst(near_lst의 16제곱), lst, lst, lst, lst] 이걸 리턴
# 17이면 아래에서 5번째가 가장 큰 1이 위치해있으므로...


# 얘도 잘 됨!
# 4, [[1,2],[3,4]] -> [-1, -1, -1, -1, [[199, 290], [435, 634]], [[7, 10], [15, 22]], [[1, 2], [3, 4]]]
def return_cache_mullist(d, near_lst):
    basic_return_list = [-1,-1,-1,-1,-1,-1,near_lst]
    
    # base case
    if d==1:
        return basic_return_list
    
    cache_numlist = dec_to_bin(d)
    largest_index = cache_numlist.index(1)
    
    # 7-1-largest_index임. largest_index가 2면,[0,0,1,0,0,0,1]에서 1의자리부터 2,4,8,16 총 4번의 제곱과정
    # 이 필요하므로...
    
    for i in range(6-largest_index):
        basic_return_list[5-i] = Matrix_mul(basic_return_list[6-i],basic_return_list[6-i])
        
    return basic_return_list

# 이제 return_cache_mullist를 가지고, d번 곱한 행렬 만들기
# 한 함수에 넣을 수도 있는데, 호흡이 너무 길어져서..

def d_times_array(d, near_lst):
    cache_mullist = return_cache_mullist(d, near_lst)
    cache_numlist = dec_to_bin(d)
    
    # 단위행렬 만들기
    unit_array = [[0 for _ in range(len(near_lst))] for _ in range(len(near_lst))]
    for i in range(len(near_lst)):
        unit_array[i][i] = 1
    
    
    for i in range(7):
        if cache_numlist[i] == 1:
            unit_array = Matrix_mul(unit_array, cache_mullist[i])
    
    # print(cache_mullist)
    # print(cache_numlist)
    return unit_array

   
# -------------------------------
# n은 마을 크기이자 행렬 가로세로
# d는 곱하는 횟수
# first는 첫 교도소 위치

# 이제 가로 세로가 n인 행렬을 입력받는다.

n, d, first = map(int, input().split())
near_lst = []

for _ in range(n):
    a = list(map(int, input().split()))
    near_lst.append(a)
        
# near_lst를 손봐야 한다. 
'''
0 1 1 1 0    0 1/2 1 1 0
1 0 0 0 1    1/3 0 0 0 1
1 0 0 0 0    1/3 0 0 0 0
1 0 0 0 0    1/3 0 0 0 0
0 1 0 0 0 은 0 1/2 0 0 0 으로.
'''
                   
for i in range(len(near_lst)):
    counter = 0
    for j in range(len(near_lst)):
        if near_lst[j][i] == 1:
        	counter += 1
    
    for k in range(len(near_lst)):
    	near_lst[k][i] /= counter

# 초기 list 설정                   
initiate_list = [[0] for _ in range(n)]
initiate_list[first][0] = 1
                   
# 계산!
answer = Matrix_mul(d_times_array(d, near_lst), initiate_list)
print(answer)
