
# input 조건에 따라 최대 제곱횟수는 100회이므로,
# 2진법으로 생각했을 때 7자리만 있으면 됨.
cache = [-1 for _ in range(7)]

def Matrix_mul(A, k):
