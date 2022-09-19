def Combinations(lis, k):
    
    return_lis = []
    
    if len(lis) < k:
        return return_lis
    elif k==1:
        for i in lis:
            return_lis.append([i])
        return return_lis
    elif len(lis) == k:
        return [lis]
    else:

        start_num = len(lis) - k

        for i in range(0, start_num +1):
            temp_lis = list_extend(0, lis[i], Combinations(lis[i+1:], k-1))
            for j in temp_lis:
                return_lis.append(j)
        return return_lis
        
    