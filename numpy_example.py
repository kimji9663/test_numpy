# path : numpy_example.py
# numpy 활용 예제

import numpy as np

# dot() : 행렬과 벡터의 곱하기
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x= np.array([10, 20, 30])
print(np.dot(A, x))


# 행렬을 열벡터로 변환
v1 = A[:, 0]
v2 = A[:, 1]
v3 = A[:, 2]
print(v1)
print(v2)
print(v3)
print(np.dot(x[0], v1) + np.dot(x[1], v2) + np.dot(x[2], v3))

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2], [3, 4], [5, 6]])
print(np.dot(A, B))

# 스칼라와 벡터의 곱하기
V = np.array([[1], [2], [3]])
a = 10
print(a*V)

# 연립방정식의 해 구하기
# Ax = b => x = A역행렬 * b
A = np.array([[4, 3], [3, 2]])
b = np.array([23, 16])
# A의 역행렬 구함(= 오른쪽으로 이항시키기 위함)
invA = np.linalg.inv(A)
x = np.dot(invA, b)
print(x)
print(np.allclose(np.dot(A, x), b))


# solve() 로 해를 구할 수도 있음 : 선형 방정식의 개수와 미지수의 개수가 같을 경우
x = np.linalg.solve(A, b)
print(x)


# lstsq() 로 해를 구할 수도 있음 : 선형 방정식의 개수와 미지수의 개수가 다를 경우
A = np.array([[1, 4, 3], [1, 3, 2]])
b = np.array([23, 16])
x = np.linalg.lstsq(A, b, rcond=None)[0]
print(x)

# 행렬식 |A| 구하기 : det(A) 함수 사용
A = np.array([[1, 4], [1, 3]])
print(np.linalg.det(A))

# 3 X 3 정방행령의 행렬식 구하기
A = np.array([[8, 5, 3], [4, 1, 6], [7, 10, 9]])
print(np.linalg.det(A))


score = np.array([80, 75, 100, 90, 60])
desc_index = score.argsort()[::-1]  # 내림차순 정렬
print(desc_index) # [2 3 0 1 4]
rank = np.empty_like(score) # score와 같은 크기의 빈배열 만들기
print(rank) # [0 0 0 0 0]
rank[desc_index] = np.arange(1, len(score) + 1)
print(score)
print(rank)


# 두 행렬의 곱 : dot(a, b)
# 작은 크기에 큰 크기를 곱하면 에러
# 계수 행렬
A = np.array([[8, 5, 3], [4, 1, 6], [7, 10, 9]]) # 3행 3열
# 결과 행렬
B = np.array([[0, 3], [1, 4], [2, 5]]) # 3행 2열
# 방정식의 해 구하기
print(np.dot(A, B))
print(np.dot(B, A))