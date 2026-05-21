# path : numpy_test3.py

import numpy as np

# 전치연산 :  T 속성 사용함 => 2차원배열명.T
# 2차원배열의 행과 열을 서로 바꿀 때 사용함
ar = np.array([[1, 2, 3], [4, 5, 6]])
print(ar)
print(ar.shape)
print(ar.T)  # 2행 3열을 3행 2열로 바꾼다.
print(ar.T.shape)

# 1차원 배열은 전치연산 못함
# 1차원 배열을 다차원 배열로 변경할 수 있음
# reshape() 함수사용 => 전체 크기(갯수)는 바뀌지 않음
ar = np.arange(12) # 12 : 0 ~ 11 로 초기화 됨
print(ar)
print(type(ar))
print(ar.ndim)
print(ar.size)

# 1차원 배열을 2차원으로 변경 (3행 4열로)
br = ar.reshape(3, 4)
print(br)
print(type(br))
print(br.ndim)
print(br.size)
print(br.T)  # 전치연산 3행 4열 -> 4행 3열(T속성으로)
print(np.transpose(br))   # 전치연산 3행 4열 -> 4행 3열 (np메소드로)
print(np.swapaxes(br, 0, 1))   # 전치연산 3행 4열 -> 4행 3열 (np메소드로)

# reshape() 사용시에 면, 행, 열 갯수를 지정하지않고, -1로 표기할 수도 있다.
# -1로 표시된 항목은 내부 계산에 의해 갯수가 자동 설정이 된다.
br2 = ar.reshape(3, -1) # 행만 정해 줬을 때 열을 -1로 하면 자동 계산되어 할당됨
print(br2) # 3행 4열

# 1차원 배열을 3차원으로 변경 (3행 4열로)
br3 = ar.reshape(2, 2, -1)
print(br3)
print(type(br3))
print(br3.ndim)
print(br3.size)

br4 = ar.reshape(2, -1, 3)
print(br4)  # 같은 결과
print(type(br4))
print(br4.ndim)
print(br4.size)


# flatten() 함수, ravel() 함수
# 다차원배열을 1차원배열로 바꿀 때 사용하는 함수
print('br:', br.shape)
print(br.flatten())
print(br.ravel()) # 같은 결과

print('br3:', br.shape)
print(br3.flatten())
print(br3.ravel()) # 같은 결과

# newaxis() 함수
# 배열의 차원을 1증가 시키는 함수
# 1차원배열 => 2차원배열 => 3차원배열
# 예) 값의 갯수가 5개인 1차원배열을 2차원배열로 바꿀 때 (5, 1) | (1, 5)로 변경 가능함
# 1차원배열 [값5개]와 2차원배열 [[값5개]]는 다름
xr = np.arange(5) # 5개 : 0 - 4까지의 정수 수열로 초기화된 배열 객체 생성됨
print(xr)
print(xr.shape) #(5,)
print(xr.reshape(1, 5))
print(xr.reshape(5, 1))

# 총 값의 갯수가 
print(xr[:, np.newaxis]) # [행, 열] 을 의미함. 콜론(:)의미는 모두 다 = Select All
# 열이 행이 됨 => 5행 1열이 됨
print(xr[np.newaxis, :])
print(xr[np.newaxis, :].shape)


