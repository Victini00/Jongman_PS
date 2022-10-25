def ip(n, queries):
    # -1은 할당 x. 그 외는 할당된 컴퓨터? 번호가 들어감
    cache = [-1 for _ in range(n)]
    is_using = [0 for _ in range(n)]
    is_haldang = [0 for _ in range(10)]
    result = []
    for i in queries:
        desktop = i.split()[0]
        desktop_num = desktop[-1]
        request_type = i.split()[1]

        if request_type == 'request':
            if is_haldang[int(desktop_num)] == 0:
                n_index = -1

                for j in range(n):
                    if cache[k] == -1:
                        n_index = k + 1
                        is_haldang[int(desktop_num)-1] = 1
                        is_using[int(desktop_num)-1] = 1
                        break

                if n_index == -1:
                    for k in range(n):
                        if is_using[k] == 0:
                            

            

            if n_index == -1:
                result.append(desktop +' '+'reject')
            else:
                cache[n_index-1] = desktop_num
                result.append(desktop +' '+'192.168.0.' +str(n_index))
            
        else:
            n_index = -1

            for j in range(n):
                if desktop_num == cache[j]:
                    n_index = j

            if n_index == -1:
                pass
            else:
                cache[n_index] = -1
                
            

    return result

print(ip(2, ['desktop1 request', 'desktop2 request', 'desktop1 release', 'desktop2 release', 'desktop3 request', 'dekstop3 release','desktop2 request', 'desktop1 request']))