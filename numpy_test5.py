# path : numpy_test5.py

# 기본 삼각함수 사용하기

import numpy as np
import matplotlib.pyplot as plt

# 사인 곡선 그래프 그리기
x = np.linspace(-5, 5, 50) # -5와 5사이에 50개의 데이터를 무작위로 뽑는다
sin = np.sin(x)
plt.plot(x, sin, label='sine')
plt.legend()
# plt.show()

# 역삼각 함수 그래프 그리기
x2 = np.linspace(-5, 5, 50) # -5와 5사이에 50개의 데이터를 무작위로 뽑는다
arcsin = np.arcsin(x2)
plt.plot(x2, arcsin, label='arcsine')
plt.legend()
# plt.show()

# 인덱스 배열 (indexed array) : 펜시 인덱싱(fancy indexing)
# 일반적인 값 추출을 위한 배열 인덱싱은 배열변수[인덱스순번]
# numpy 가 제공하는 다른 표현의 배열 인덱싱 방식임

# bool 배열 인덱싱과 정수 배열 인덱싱 방식 2가지 있음
# 인덱싱을 위한 별도 배열을 만들어서 사용하는 방식임
# 주의 : 값을 가진 인덱싱 대상과 인덱싱을 위한 배열의 크기(갯수)가 반드시 일치해야함

# 1. bool 배열 인덱싱으로 배열값 추출하기
# True, False로 이루어진 배열 만듦 => 값 추출할 인덱싱 위치에 True를 지정하는 방식
# 예 : 홀수 값들이 있는 위치 지정으로 홀수 값들만 추출하는 경우
ar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
idx_array = np.array([True, False, True, False, True, False, True, False, True, False])
print(ar[idx_array]) # 배열변수[인덱싱배열명]  # True 위치의 값만 뽑아내짐

# 벡터화 연산 또는 조건문 연산을 사용할 수도 있음
print(ar % 2) # ar[0] % 2, ar[1] % 2, ar[2] % 2, ...
# [1 0 1 0 1 0 1 0 1 0]  1이 True, 0이 False
# 이 결과값을 연산에 이용할 수 있음

print(ar % 2 == 0)  # ar[0] % 2 == 0, ar[1] % 2 == 0, ar[2] % 2 == 0, ...
# [False  True False  True False  True False  True False  True]  
# 아까처럼 직접만드는 대신 위와 같은 연산으로 True False 배열을 만들수도 있음
print(ar[ar % 2 == 0])  # True인 짝수 값만 골라냄


# 2. 정수 배열 인덱싱
# 인덱싱을 위한 배열을 만들 때, 추출할 인덱스 위치에 대한 숫자를 배열로 만듦
ar2 = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx_array2 = np.array([0, 2, 5, 7, 8]) # 골라낼 인덱스 숫자 표기
print(ar2[idx_array2]) # [11 33 66 88 99]
# 특정한 규칙이 없는 값을 골라내고자 할 때 사용할 수 있음


# 정수 인덱싱 배열은 크기가 대상 배열의 크기와 일치하지 않아도 됨
# 값을 가진 대상 배열보다 크기가 커도 됨
idx_array3 = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2])
print(ar2[idx_array3]) # [11 11 11 11 22 22 22 22 22 33 33 33 33]
# 정수 인덱싱 배열은 배열 갯수 안맞춰도 됨


# 배열 인덱싱은 다차원배열의 각 차원에 대해서도 적용할 수 있음
ar3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # 3행4열
print(ar3)
print(ar3[:, True, False, False, True])  # [모든행, [bool값]] 각 행의 0열, 3열
print(ar3[[2, 0, 1], :])  # [[숫자값], 모든열]  2행 0행 1행 순으로 모든 열값 추출


# 데이터 샘플링 (표본 추출) : choice() 함수 사용
# np.random,=.choice(a, size=None, replace=True, p=None)
# a : 배열변수 (배열값을 사용해도 됨), 정수숫자(range(정수) 범위의 랜덤값을 만듦)
# size : 정수숫자, 추출할 데이터 갯수 지정
# replace : True | False, 같은 값 여러번 선택 가능(True) | 불가능(False) 여부 지정
# p : 배열 변수나 배열표기, 각 값의 선택 확률을 지정함 (단, 확률의 합계는 1이어야함)

ch1 = np.random.choice(5, 5, replace=False)  # 0에서 5까지의 수 중에 무작위(shuffle) 5개, 중복허용안함
print(ch1)
print(type(ch1)) # <class 'numpy.ndarray'>

ch2 = np.random.choice(5, 3, replace=False)  # 0에서 5까지의 수 중에 무작위(shuffle) 3개, 중복허용안함
print(ch2)
print(type(ch2))

ch3 = np.random.choice(5, 10, p=[0.1, 0, 0.3, 0.6, 0])  # 0에서 5까지의 수 중에 무작위(shuffle) 10개, 중복허용, 값선택확률지정
print(ch3) # [0 0 3 2 3 3 0 0 3 3]  비중이 항상 같게 나오는 것은 아닌듯... 10%인 0이 30%인 2보다 많이 나옴
print(type(ch3))

# numpy에서 제공되는 난수생성함수 3가지
# rand, randn, randint
# rand(겟수): 0.0 <= 난수 < 1.0 사이의 균일한 확률분포로 난수를 갯수만큼 발생
r1 = np.random.rand(10)
print(r1)
print(type(r1))

r2 = np.random.rand(3, 5) # 3행 5열의 2차원배열 생성하고 15개의 난수 발생
print(r2)
print(type(r2))

# randn(갯수)
# 기댓값이 0이고 표준편차가 1인 표준정규분포를 따르는 난수를 생성함
# 표준정규분포 : 숫자들이 가운데로 많이 모이고 가장자리로 갈수록 적어짐
# 기댓값 : 평균
# 숫자들이 0을 중심으로 모여있다는 의미
# 표준편차 : 값이 퍼져있는 정도(평균의 차이, 표준편차가 1이면 -1 <= 0 <= 1 범위의 값이 많이 모여있다는 의미)
r3 = np.random.randn(10)
print(r3)
print(type(r3))
print(r3.shape)

r4 = np.random.randn(3, 5)  # 3행 5열의 2차원배열 생성
print(r4)
print(type(r4))
print(r4.shape)


# randint(low, high=None, size=None)
# low <= 난수 < high 사이의 정수를 size 갯수만큼 발생시킨 배열 생성
# high가 생략되면, 0 - low 까지의 범위에서 값 발생
r5 = np.random.randint(10, size=10) # 0 <= 정수난수 < 10 사이의 정수 10개 발생
print(r5)
print(type(r5))
print(r5.shape)

r6 = np.random.randint(10, 20, size=10) # 10 <= 정수난수 < 20 사이의 정수 10개 발생
print(r6)
print(type(r6))
print(r6.shape)

r6 = np.random.randint(10, 20, size=(3, 5)) # 10 <= 정수난수 < 20 사이의 정수 15개 2차원 배열로 발생
print(r6)
print(type(r6))
print(r6.shape)

