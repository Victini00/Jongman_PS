# 종만북 fanmeeting의 테스트 자료임.
def normalize(n):
  # 역 상태의 행렬을 자릿수 정리 후 정출력
  # len(c) - 1인 이유: 맨 윗자리는 절대로 올림이 없고,
  # 있어도 index에러가 뜸(i+1이 존재하지 않으므로.)
  for i in range(len(n)-1):
    if n[i] < 0:
      borrow = (abs(n[i]) + 9) // 10
      n[i+1] -= borrow
      n[i] += borrow * 10
    else:
      n[i+1] += n[i] // 10
      n[i] %= 10

  # 이제 정출력
  n.reverse()
  for i in range(len(n)):
    if n[i] != 0:
      return n[i:]

  return n

print(normalize([49,84,106,60,25,0]))