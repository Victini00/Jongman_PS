num_array = list(map(int,input().split()))

memory_array = []
index_array = []

LIS_array = []

for i in num_array:
    # 맨 처음은 일단 넣고 시작
    if not memory_array:
        memory_array.append(i)
        index_array.append(1)
        
    elif memory_array[-1] < i:
        # 아래 2개의 순서 주의!
        index_array.append(len(memory_array)+1)
        memory_array.append(i)
                
    else:
        for j in range(len(memory_array)):
            if i <= memory_array[j]:
                memory_array[j] = i
                index_array.append(j+1)
                break
                
LIS_len = len(memory_array)

# -2임에 주의!
for i in range(-1,-(LIS_len)-2,-1):
    if index_array[i] == LIS_len:
        LIS_array.insert(0, num_array[i])
        LIS_len -= 1

print(num_array) # 입력받은 원래 배열.
print(memory_array) # K. 크기에 따라 삽입한 거. 이거의 길이가 JLIS의 길이가 된다.
print(index_array) # 인덱스 배열이다.
print(LIS_array) # JLIS 배열 즉 답.

                
