# path : numpy_test1.py
# numpy모듈 : 배열을 다루기 위한 모듈

'''
배열과 리스트의 차이
1. 배열 : 처음부터 저장할 갯수를 지정, 리스트 : 저장 갯수에 제한 없음
2. 배열 : 한가지 종류의 값만 저장, 리스트 : 여러종류를 저장 가능
3. 배열 : 저장 순번을 사용함, 리스트 : 저장 순번을 사용함
'''

import numpy as np

# 1차원 배열 다루기: numpy.array([한가지 종류로만 저장된 리스트]) => 리스트를 배열로 바꿈
# 배열변수 = np.array([리스트])
# 배열변수는 배열객체의 주소를 가짐 : 배열 레퍼런스(주소 저장 변수임)
# 주로 정수 | 실수 | 논리값으로 구성됨

ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ar)
print(ar.dtype, type(ar))  # int64 <class 'numpy.ndarray'> 배열을 뜻함
print(len(ar))

# 배열은 벡터화 연산이 가능하다.
# 벡터화 연산이란, 각 인덱스별로 연산하는 것
# 리스트 일 때 벡터화 연산 처리 예 :
datalist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(datalist)) # <class 'list'>

# 리스트 안의 값 2배 증가처리 연산
double_datalist = []
for data in datalist:
    double_datalist.append(data * 2)
print(double_datalist)

# 위의 처리를 배열로 바꿔서 벡터화 연산을 처리 한다면
print(ar * 2)

# 배열의 벡터화 연산은 비교연산, 논리연산, 산술연산 모두 가능
# Ndarray 클래스에 각 연산자에 대한 연산자오버로딩 메소드가 정의 제공되어 있기 때문
ar1 = np.array([1, 2, 3])
br1 = np.array([10, 20, 30])

print(2 * ar1 + br1) # ar1[0] * br1[0]...
# [12 24 36]

print(ar1 == 2) # [False  True False]

print((ar1 == 2) & (br1 > 10)) 
# [False True False] & [False True True]두 연산 결과 : [False  True False]


# 1차원 배열의 각 인덱스 위치의 값(요소, element)에 접근 : 인덱싱(indexing)
for index in range(0, ar.size):
    print(index, ':', ar[index])

