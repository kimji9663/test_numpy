# path : numpy_test8.py

import numpy as np

# 배열 생성과 초기화 동시에 처리하는 함수 확인
# 초기값 : 변수 공간에 첫번째로 기록되는 값
# 변수 공간 만들면서 바로 초기값 기록하는 것을 초기화라고 함
# np.array([리스트]) => 리스트 값들로 초기화 함

# zeros() : 배열 생성시 0으로 초기화함
# 사용 : 배열변수 = np.zeros(배열할당갯수) => 1차원배열 생성하고, 0으로 초기화함
# 사용 : 배열변수 = np.zeros((행갯수, 열갯수)) => 2차원배열 생성하고, 0으로 초기화함
# 사용 : 배열변수 = np.zeros((면갯수, 행갯수, 열갯수)) => 3차원배열 생성하고, 0으로 초기화함
ar = np.zeros(5)
print(ar) # [0. 0. 0. 0. 0.]
print(ar.dtype) # float64
print(ar.ndim) # 1
print(ar.shape) # (5,)

br = np.zeros((2, 3))
print(br) # [[0. 0. 0.] [0. 0. 0.]]
print(br.dtype) # float64
print(br.ndim) # 2
print(br.shape) # (2, 3)


cr = np.zeros((5, 2), dtype='i4')
print(cr) # [[0 0] [0 0] [0 0] [0 0] [0 0]]
print(cr.dtype) # int32
print(cr.ndim) # 2
print(cr.shape) # (5, 2)

dr = np.zeros(5, dtype='U4')
print(dr) # ['' '' '' '' '']
print(dr.dtype) # <U4
print(dr.ndim) # 1
print(dr.shape) # (5,)

dr[0] = 'abc'
dr[1] = 'abcd'
dr[2] = 'ABCDE'
print(dr) # U4는 4글자 까지만 기록됨 => 5번째 글자인 E는 기록 안됨

# ones() 함수
# 배열 생성하면서, 1로 초기화
er = np.ones((2, 3, 4), dtype='i8')  # 2면 3행 4열 3차원배열, 정수 1로 초기화함
print(er)

# zeros_like(), ones_like() 함수
# 다른 배열과 같은 크기(shape)의 배열을 생성하면서 초기화
# 예) 2행 3열인 2차원배열인 br과 같은 크기(shape)의 배열을 생성하려면
fr = np.ones_like(br, dtype='f')
print(fr)
print(br.shape, fr.shape) # (2, 3) (2, 3) : shape이 같음

# empty() 함수
# 값이 없는 빈 배열 생성시 사용함 => 배열 생성이 빠름
gr = np.empty((4, 3))
print(gr)

# arange() 함수
# 파이썬의 range() 함수와 같음
# 배열 생성시에 지정한 범위의 값들을 초기값으로 기록해 넣을 때 사용함
# 시작값, 종료값, 증가치를 설정하면, 규칙에 따라 수열을 만듦
hr = np.arange(10) # 10개 : 0 - 9까지의 정수를 수열로 초기화함
print(hr)

hr2 = np.arange(3, 21, 2) # 종료값 -1 까지의 숫자가 발생
print(hr2) 

# linespace(), logspace() 함수
# linespace(시작값, 끝값, 구간갯수)
# logspace(시작값, 끝값, 구간갯수)
ir = np.linspace(0, 100, 5) # 0부터 100까지를 5구간으로 나눈 값을 초기값으로 함
print(ir) # [  0.  25.  50.  75. 100.]

ir2 = np.logspace(0.1, 1, 10) # 10의 0.1제곱(약 1.26)부터 10의 1제곱(10)까지를 10개로 나눈 값을 초기값으로 함
print(ir2) # [ 1.25892541  1.58489319  1.99526231  2.51188643  3.16227766  3.98107171  5.01187234  6.30957344  7.94328235 10.        ]
# log : 어떤 수를 만들기 위해 몇번 곱했는지? 곱한 횟수
# 예) 2를 몇번 곱해야 8일 되는가? => 3
# 상용로그 : 밑이 10인 로그
# log10(100) => 답 : 2
# 자연로그 : 밑이 e인 로그
# ln(x)
