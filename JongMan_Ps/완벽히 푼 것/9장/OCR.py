#OCR_refactoring
#조금 더 깔끔하게...

# -----inputs------------------------------------------------------

word_len = int(input())
word_list = list(input().split())

# 처음 단어가 올 확률
B_matrix = list(map(float, input().split()))
# i 다음 단어가 j일 확률
T_matrix = []
# i번 단어가 적힌 조각을 j번 단어로 구분할 확률
M_matrix = []

for _ in range(word_len):
    temp_T_list = list(map(float, input().split()))
    T_matrix.append(temp_T_list)
    
for _ in range(word_len):
    temp_M_list = list(map(float, input().split()))
    M_matrix.append(temp_M_list) 

identify_sentence = list(input().split())
sen_len = len(identify_sentence)

# -----input example-----------------------------------------------
'''
5
i am a boy buy
1.0 0.0 0.0 0.0 0.0
0.1 0.6 0.1 0.1 0.1
0.1 0.1 0.6 0.1 0.1
0.1 0.1 0.1 0.6 0.1
0.2 0.2 0.2 0.2 0.2
0.2 0.2 0.2 0.2 0.2
0.8 0.1 0.0 0.1 0.0
0.1 0.7 0.0 0.2 0.0
0.0 0.1 0.8 0.0 0.1
0.0 0.0 0.0 0.5 0.5
0.0 0.0 0.0 0.5 0.5
i am a buy
'''
# -----------------------------------------------------------------

# sen_cache의 역할: 이전 단어가 a 일때, 가장 확률이 높은 다음 단어 b를 저장해줘서,
# 문장을 출력하는 데 추적할 수 있게 해준다.
sen_cache = [[-1 for _ in range(sen_len)] for _ in range(word_len)]

# cache는 평범하게 
cache = [[-1 for _ in range(sen_len)] for _ in range(word_len)]

# 가능성이 제일 높은 원래 문장을 찾는 함수
def probab(word, seq):
    
    word_index = word_list.index(word) if seq != 0 else 0
    
    # base case
    if seq == sen_len:
        return 1
    
    # memoization
    if cache[word_index][seq] != -1:
        return cache[word_index][seq]
    	
    # main
    
    max_prob = 0
    
    for i in word_list:
        mem = max_prob
        next_probab = probab(i, seq+1) * M_matrix[word_list.index(i)][word_list.index(identify_sentence[seq])]
        
        if seq == 0:
            max_prob = max([max_prob, B_matrix[word_list.index(i)] * next_probab])
            
        else:
            max_prob = max([max_prob, T_matrix[word_index][word_list.index(i)] * next_probab])
        
        if mem != max_prob:
            sen_cache[word_index][seq] = i
        
        cache[word_index][seq] = max_prob
        
    
    return cache[word_index][seq]

# 문장을 출력해주는 함수
def making_sentence():
    total_sentence = []
    next_word = 0
    
    next_word = sen_cache[next_word][0]
    total_sentence.append(next_word)
    
    for i in range(1, sen_len):
        # 맨 처음 단어를 어케할까
        next_word = sen_cache[word_list.index(next_word)][i]
        total_sentence.append(next_word)
        
    return total_sentence

# ----------------------------------
probab('*', 0)
print(making_sentence())
    
# --output example-------------------
'''
['i','am','a','boy']
'''
