# path : numpy_test6.py

import numpy as np

# 기술 통계(descriptive staticstatics) : 통계 계산용 함수를 말함
# 데이터 갯수(count), 평균(mean, average), 분산(variance), 표준편차(standard deviation)
# 최대값(maximum), 최소값(minimum), 중앙값(median), 사분위수(quartile)

x = np.random.randint(-10, 50, size=30)
print(x)

# 데이터 갯수
print('len :', len(x))

# 평균 : np.mean(배열변수)
print('mean :', np.mean(x))

# 표본 분산(sample varience) : 데이터와 평균 간의 거리의 제곱의 평균
print('var :', np.var(x))
print('var ddof :', np.var(x, ddof=1))  # 비편향분산 (값이 한쪽으로 쏠리지 않게 분산)

# 표준 편차 : 표본 분산의 양의 제곱근, ss라고 표시함
print('ss :', np.std(x))

# 최대값, 최소값, 중앙값
print('max :', np.max(x))
print('min :', np.min(x))
print('median :', np.median(x))

# 사분위수
# 데이터를 오름차순정렬했을 때, 1/4, 2/4(중앙값), 3/4, 4/4(최대값)  위치의 값
# 1사분위, 2사분위, 3사분위, 4사분위
# 데이터 갯수가 100개이면, 1사분위는 25번째 값이 됨
print(np.percentile(x, 0)) # 최소값
print(np.percentile(x, 25)) # 1사분위 1/4
print(np.percentile(x, 50)) # 2사분위 2/4
print(np.percentile(x, 75)) # 3사분위 3/4
print(np.percentile(x, 100)) # 4사분위 4/4

# np.random.seed(인수)
# seed : 난수의 시작값
# 인수 : 정수 >= 사용함
# print(np.random.rand(5))
# -10.0  0.0  13.0  32.75  49.0
# -10.0  12.25  20.5  34.5  47.0
# 매번 다른 값 발생

# 설정 이후 한번 발생된 랜덤값으로 동일하게 값 발생
np.random.seed(0)
print('seed 후 rand :', np.random.rand(5))

# 데이터 섞기 : shuffle()
x = np.arange(10)
print(x)
np.random.shuffle(x)
print(x)


