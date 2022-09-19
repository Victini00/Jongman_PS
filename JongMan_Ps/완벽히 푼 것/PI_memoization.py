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

lis = input()
cache = [-1 for _ in range(len(lis))]


def PI(num):
    standard = len(lis) - num
    if standard < 3:
        return -1
    elif standard >=3 and standard <= 5:
        return difficulty(lis[num:])
    elif standard == 6:
        return difficulty(lis[num:num+3]) + difficulty(lis[num+3:])
    elif standard == 7:
        min_diff = min([difficulty(lis[num:num+3]) + difficulty(lis[num+3:]),
                        difficulty(lis[num:num+4]) + difficulty(lis[num+4:])])
        return min_diff
    else:
        cache[num+3] = PI(num+3) if cache[num+3] == -1 else cache[num+3]
        cache[num+4] = PI(num+4) if cache[num+4] == -1 else cache[num+4]
        cache[num+5] = PI(num+5) if cache[num+5] == -1 else cache[num+5]

        min_diff = min([difficulty(lis[num:num+3]) + cache[num+3],
                        difficulty(lis[num:num+4]) + cache[num+4],
                        difficulty(lis[num:num+5]) + cache[num+5]])
        return min_diff


print(PI(0))




