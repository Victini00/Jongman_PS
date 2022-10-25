# 3~5 길이의 list input에 대하여 난이도를 계산하는 함수
def difficulty(lis):
    lis_len = len(lis)

    sub_list = [0 for _ in range(lis_len-1)]
    sub_len = len(sub_list)

    for i in range(lis_len-1):
        sub_list[i] = int(lis[i]) - int(lis[i+1])

    # 이제 sub list를 돌며 난이도를 확인한다.
    if sub_list.count(0) == sub_len:
        return 1
    
    elif sub_list.count(1) == sub_len or sub_list.count(-1) == sub_len:
        return 2

    elif lis.count(lis[0]) + lis.count(lis[1]) == lis_len:
        return 4

    elif sub_list.count(sub_list[0]) == sub_len:
        return 5
    
    else:
        return 10
'''
print(difficulty([3,3,3]))
print(difficulty([5,5,5,5]))
print(difficulty([2,3,4,5,6]))
print(difficulty([3,2,1,0]))
print(difficulty([3,2,3]))
print(difficulty([5,4,5,4,5]))
print(difficulty([1,4,7]))
print(difficulty([8,6,4,2]))
print(difficulty([3,3,1]))
'''

def PI(lis):
    if len(lis) < 3:
        return -1
    elif len(lis) >=3 and len(lis) <= 5:
        return difficulty(lis)
    elif len(lis) == 6:
        return difficulty(lis[0:3]) + difficulty(lis[3:])
    elif len(lis) == 7:
        min_diff = min([difficulty(lis[0:3]) + difficulty(lis[3:]),
                        difficulty(lis[0:4]) + difficulty(lis[4:])])
        return min_diff
    else:
        min_diff = min([difficulty(lis[0:3]) + PI(lis[3:]),
                        difficulty(lis[0:4]) + PI(lis[4:]),
                        difficulty(lis[0:5]) + PI(lis[5:])])
        return min_diff

input_num = int(input())
N = list(input() for _ in range(input_num))
for i in N:
    global cache 
    cache = [-1 for _ in range(len(i))]
    print(PI(i))

