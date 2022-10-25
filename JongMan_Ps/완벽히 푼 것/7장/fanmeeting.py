def multiply(x, y):
  # 정입력 받고, 역입력으로 바꾼 뒤, normalize처리해서 정출력.
  x.reverse()
  y.reverse()
  z = [0 for _ in range(len(x)+len(y))]
  for i in range(len(x)):
    for j in range(len(y)):
      z[i+j] += x[i] * y[j]
  
  #혹시 모르니 x랑 y 원상복구
  x.reverse()
  y.reverse()
  return normalize(z)

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

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# print(multiply(a,b))

def karatsuba(a, b):
  # 정입력
  if len(a) < len(b): 
    return karatsuba(b,a)
  if a == [0] or b == [0]:
    # b1이 []이 되는 경우 생각.
    return [0]
  if len(a) <= 5:
    return multiply(a,b)

  # 기저 사례 끝.. 이제..
  # expo와 half를 잘 구분해야 함.
  # a의 길이가 짝수일 때와 홀수일 때를 잘 보자.
  half = (len(a) // 2) + (len(a) % 2)
  expo = (len(a) // 2)
  # a1이 앞쪽(큰자리).  정입력받앗음에 주목.
  a1 = a[0:half]
  a0 = a[half:]

  if len(b) <= expo:
    b0 = b
    b1 = [0]
  else:
    b1 = b[:len(b)-expo]
    b0 = b[len(b)-expo:]

  # remind! 정입력이고, a1과 b1은 절반 잘랐을때 앞자리(큰자리수)
  

  z2 = karatsuba(a1,b1)
  z0 = karatsuba(a0,b0)
  new_a0 = addTo(a0, a1, 0)
  new_b0 = addTo(b0, b1, 0)  
  z1 = karatsuba(new_a0,new_b0)
  z1_memory = subFrom(z1,z0)
  z1_memory2 = subFrom(z1_memory,z2)

  ret = [0]
  ret = addTo(ret,z0,0)
  ret = addTo(ret,z1_memory2,expo)
  ret = addTo(ret,z2,2*expo)
  return ret

def addTo(a,b,k):
  # 수열을 입력받음.. 정입력
  # c 수열 길이의 max 주의!!
  c_length = max([len(a), len(b)+k])
  c = [0 for _ in range(c_length)]
  for i in range(-1,-1-len(a),-1):
    c[i] = a[i]

  for i in range(-1,-1-len(b),-1):
    c[-k+i] += b[i]

  c.reverse()

  # normalize와 비슷
  # 그러나 맨 윗자리에서 올림 발생 확률 존재
  # 그 경우를 추가로 생각.
  for i in range(len(c)-1):
    if c[i] < 0:
      borrow = (abs(c[i]) + 9) // 10
      c[i+1] -= borrow
      c[i] += borrow * 10
    else:
      c[i+1] += c[i] // 10
      c[i] %= 10

  # 맨 윗자리 생각
  # 음수 배제
  if c[-1] < 10:
    c.reverse()
    return c
  elif c[-1] >= 10:
    c_up = c[-1] // 10
    c[-1] %= 10
    c.append(c_up)
    c.reverse()
    return c

def subFrom(a,b):
  # 마찬가지로 정입력
  len_difference = len(a) - len(b)
  optimized_b = [0 for _ in range(len_difference)] + b
  c = [0 for _ in range(len(a))]
  for i in range(len(c)):
    c[i] = a[i] - optimized_b[i]

  for i in range(-1,-len(c),-1):
    # 뺄셈이니까 올림이 있는 경우는 없다.
    # 정 정렬 상태로 그냥 올림 처리.
    if c[i] < 0:
      borrow = (abs(c[i]) + 9) // 10
      c[i-1] -= borrow
      c[i] += borrow * 10

  for i in range(len(c)):
    if c[i] != 0:
      return c[i:]


# ---------------------------------
# test case 

print(karatsuba([1,2,3,4,5,6,7],[1,2,3,4,5]))