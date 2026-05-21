# path : numpy_test2.py
# numpy는 Ndarray 클래스를 사용함 : C언어로 만든 내부 로직을 제공함
# type을 확인하면, 배열의 자료형은 nuppy.Ndarray
# Ndarray : N-Dimensional Array 줄임말(N차원 배열)
# 1차원 배열부터 다차원 배열을 다룰 수 있음

import numpy as np

# 2차원 배열 만들기
# 1차원 배열 여러개(그러나 값의 갯수는 동일하게)를 묶으면 2차원 배열이다.
# 1차원 배열 : 벡터(vector)
# 2차원 배열 : 메트릭스(matrix) : 행과 열로 구성된 행렬(표) 형태
# [[리스트], [리스트], [리스트] ...] : list of list 형태일 것(단, 리스트 안의 값 갯수가 동일해야함)

tar = np.array([[0, 1, 2], [3, 4, 5]]) # 2행 3열 2차원 배열
print(tar)
# [[0 1 2]
#  [3 4 5]]
print(len(tar)) # 행 갯수
# 2
print(len(tar[0])) # 3 : 0 행 안의 값(열) 갯수
# 3
print(tar.size, np.size(tar)) # 모든 갯수 구하기
# 6 6

# 2차원 배열의 각 값(요소)에 접근 (인덱싱) : 배열변수[행순번][열순번]
# 행(row, 제2축) : 세로방향 순번
# 열(column, 제1축) : 가로방향 순번
# 2중 for문 사용
for r_index in range(len(tar)):  # 행
    for c_index in range(len(tar[r_index])): # 열
        print('tar[{}][{}] : {}'.format(r_index, c_index, tar[r_index][c_index]))

# 3차원 배열 만들기
# 2차원 배열 여러개(그러나 값의 갯수는 동일하게)를 묶으면 3차원 배열이다.
# 면(깊이, depth), 행(줄, row, 높이, height), 열(칸, column)로 구성됨 => Tensor(텐서)라고 함
# [[[리스트], [리스트]], [[리스트], [리스트]] ...] : list of list 형태일 것(단, 리스트 안의 값 갯수가 동일해야함)
thar = np.array([
        [
            [1, 2, 3, 4], # 1행
            [5, 6, 7, 8], # 2행
            [9, 10, 11, 12] # 3행
        ], # 0면
        [
            [13, 14, 15, 16], # 1행 
            [17, 18, 19, 20], # 2행 
            [21, 22, 23, 24] # 3행
        ], # 1면
    ])
# 2면 3행 4열
print(thar)
print(len(thar))
print(len(thar[0]))
print(len(thar[1]))
print(len(thar[0][0]))

# 3차원배열 안의 각 값(요소)를 다루려면 (인덱싱) : 배열변수[면순번][행순번][열순번]
# 3중 for문 사용
for didx in range(len(thar)): # 면반복 : range(2) => 0, 1
    for ridx in range(len(thar[didx])): # 행반복 : range(3) => 0, 1, 2
        for cidx in range(len(thar[didx][ridx])): # 열반복 : range(4) => 0, 1, 2, 3
            print('thar[{}][{}][{}] : {}'.format(didx, ridx, cidx, thar[didx][ridx][cidx]))
        print('---------------------------------------------------------')

# 배열의 차원(ndim)과 크기(shape) 알아내기
# 배열변수 .ndim, 배열변수 .shape
print(tar.ndim) # 2
print(tar.shape) # 투플로 리턴 : (2, 3) # 2행 3열을 의미
print(thar.ndim) # 3
print(thar.shape) # (2, 3, 4) # 2면 3행 4열을 의미

# 1차원 배열의 ndim, shape 확인
ar = np.array([1, 2, 3])
print(ar.ndim) # 1
print(ar.shape) # (3,)

# 2차원 배열의 인덱싱 : 배열변수[행순번][열순번] === 배열변수[행순번, 열순번]
# 콤마(,)를 이용할 수도 있다 => 축(axis)라고 함
# 행(x축), 열(y축)
print('0행 0열의 값 : ', tar[0][0], tar[0, 0])
print('1행 0열의 값 : ', tar[1][0], tar[1, 0])
print('마지막행 마지막열의 값 : ', tar[-1][-1], tar[-1, -1])  # 5 5

# 한가지로 채우는 생성 함수들
arr = np.ones((2, 3)) # 많이씀
print(arr.ndim)
print(arr.shape)
print(arr)

arr = np.zeros((2, 3)) # 많이씀
print(arr.ndim)
print(arr.shape)
print(arr)

arr = np.full((2, 3), 10)
print(arr.ndim)
print(arr.shape)
print(arr)

arr = np.empty((2, 3))
print(arr.ndim)
print(arr.shape)
print(arr)