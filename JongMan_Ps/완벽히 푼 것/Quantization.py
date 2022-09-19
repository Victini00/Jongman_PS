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
        

def list_extend(space, a, lis):
    for i in lis:
        i.insert(space,a)
    return lis

# print(Combinations([1,2,3,4,5,6],4))

def calculate_int_mean(lis):
    len_lis = len(lis)
    total_sum = sum(lis)
    mean = total_sum / len_lis
    
    int_mean = round(mean)
    
    return int_mean

def calculate_min_psuedo_variance(lis):
    int_mean = calculate_int_mean(lis)
    result = 0
    for i in lis:
        result += pow((i-(int_mean)), 2)
    return result

#--------------------------------

def Quantization(lis, k):
    #base case
    if k==1:
        return calculate_min_psuedo_variance(lis)

    lis.sort()
    len_lis = len(lis)
    
    cache = [[-1 for _ in range(len_lis+1)] for _ in range(len_lis+1)]
    
    Comb_list = Combinations([i for i in range(1,len_lis)], k-1)
    Comb_list = list_extend(k-1, len_lis, Comb_list)
    
    final_result = 123456789 # 유사 inf.
    
    for i in Comb_list:
        
        check_sum = 0
        first_num = 0
        
        for j in i:
            check = cache[first_num][j]
            if check != -1:
                check_sum += check
            else:
                temp = calculate_min_psuedo_variance(lis[first_num:j])
                cache[first_num][j] = temp
                check_sum += temp
                
                # initialization
                first_num = j
                
        final_result = min([final_result, check_sum])
        
    return final_result
                
            
    
    
print(Quantization([3,3,3,1,2,3,2,2,2,1],3))
    
    
    