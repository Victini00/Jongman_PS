# 3~5 길이의 list input에 대하여 난이도를 계산하는 함수
inf = 987654321

def difficulty(lis):

    lis_len = len(lis)
    if lis_len < 3:
        return inf

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

lis = input()
# len(lis)+1 에서 +1에 주의(indexerror)
cache = [-1 for _ in range(len(lis)+1)]


def PI(num):
    standard = len(lis) - num

    if standard == 0:
        return 0

    elif standard < 3:
        return inf

    else:
        min_diff = inf
        for i in range(3,min([6,standard+1])):
            cache[num+i] = PI(num+i) if cache[num+i] == -1 else cache[num+i]
            min_diff = min([min_diff, difficulty(lis[num:num+i]) + cache[num+i]])

        return min_diff

print(PI(0))




