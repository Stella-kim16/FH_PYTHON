import numpy as np
## Create a vector with values ranging from
# # 10 to 49. Reverse a vector (first element
# # becomes last)


# vector = np.arange(10, 50)
# print(vector)
# vector2 = vector[::-1]
# print(vector2)



# # Create a 5x5 array with random values.
# # and find the minimum and maximum
# # values


# x = np.random.random((5,5))
# print("max: {}, \n min: {}".format(np.max(x), np.min(x)))
# print("shape:", x.shape)



## Normalize a 5x5 random matrix
# 일반화 시키는데 보통 ones 나 zeros 를 사용해서 만듦 

# arr = np.zeros((5,5))
# print(arr)

## Multiply a 5x3 matrix by a 3x2 matrix (real
## matrix product)


# x = np.array(np.random.random((5,3)))
# y = np.array(np.random.random((3,2)))

# z = x.dot(y)
# print(z)


# How to get the dates of yesterday, today
# and tomorrow?

# from datetime import date, timedelta

# today = date.today()

# yesterday = today - timedelta(days=1)
# tomorrow = today + timedelta(days=1)

# print("yesterday: {}, today: {}, tomorrow: {}".format(yesterday, today, tomorrow))


# 6. Extract the integer part of a random array
# using 5 different methods
# 5개의 메소드가 있는 랜덤 행렬에서 int 값만 빼내기 

# arr = np.random.rand(5) *10 
# print(arr)
# print(arr.astype(int))


# 7. Create a structured array representing a
# position (x,y) and a color (r,g,b)

# 위치와 색상을 나타내는 구조화 배열을 생성하기 
# 숫자가 나오진 않았으니 그냥 structured array 만 만든다고 하면 

# arr = np.zeros(3, dtype=[
#     ('x', 'i4'), 
#     ('y', 'i4'), 
#     ('r' ,'i4'),

# ])

# print(arr)


# 8. Consider a generator function that
# generates 10 integers and use it to build an
# array

# 10개의 정수를 생성하는 함수 만든 후 배열 만들기 

# def making ():
#     for i in range(10):
#         yield i # 숫자를 하나씩 생성하는 generator 함수 

# arr = np.fromiter(making(), dtype=int)

# print(arr)

# # 10. Consider two random array A and B, check
# # if they are equal

# a = np.random.random((2,2))
# b = np.random.random((2,2))

# if np.array_equal(a,b): # if a==b 라고 하면 안됨! 
#     print("equal")
# else: 
#     print("no")


# 11. Consider a random vector with shape
# (100,2) representing coordinates, find
# point by point distances
# 점과 점 사이의 거리를 구해라 


# points = np.random.random((100, 2))

# distances = np.sqrt(np.sum((points[1:] - points[:-1]) ** 2, axis=1))

# print(distances)

# 12. Subtract the mean of each row of a matrix
# substact - 빼다 
# 각 행의 평균값을 구한후 각 행에서 그 값을 빼라 

# arr = np.random.random((3,4))
# # 평균값구하는 함수 
# row_mean = arr.mean(axis=1, keepdims=True) # axis=1 은 행을 기준으로 평균값을 구하겠다는 의미
# # axis = 1 로 설정해야 행의 값을 기준으로 계산 

# # 각 행에서 평균값빼기 - 새로운 value 하나 만들어서 결과넣기 
# result = arr - row_mean

# print(arr, result)

# 13. How to I sort an array by the nth column?
# 배열은 nth (n)번째 기준으로 정렬하면 어떻게 되는지? 

# arr  = np.random.randint(0,10, (5,5))
# # random 값을 정수로 받고싶을때 0-10 이라고 하고 뒤에 () 배열 수 넣기
# # random 이 아니고 randint 로 들어온거 주의! 

# print(arr)
# print()

# # 예를 들어 index = 1 을 기준으로 정렬하고 싶다면 
# result = arr[arr[:, 1].argsort()]
# # column 이라고 했으니까 열을 가져와야하므로 
# # 모든행을 : 로 먼저 가져오고 임의로 2번째 열을 가져옴 0 -> 1 
# print(result)
# #argsort 그 열을 기준으로 정렬함. 


# 14. Compute a matrix rank
# 행렬의 랭크를 계산하시오 
# 랭크? 행렬에서 서로 독립적인 행 또는 열의 개수 
# 어떤 기본이 되는 행에 임의숫자를 곱해서 만들 수 있는 행렬은 rank 가 있다고 보고
# 어떤 수를 추가해도 만들수없는 즉, 관계가 없으면 rank 가 없는것 

# arr = np.random.randint(0, 10, (3, 3))
# # rank 계산
# result = np.linalg.matrix_rank(arr)
# print("matrix:\n", arr)
# # rank 는 얼마나 서로 다른 정보가 있는지 확인할때 쓴다 
# # 행렬에 몇개의 독립적인 정보가 있는지, 중복이 있는지등등 


# 15. Consider a 16x16 array, how to get the
# block-sum (block size is 4x4)

# 블럭의 합을 구해라 
# 한칸에 4*4 가 들어있는 16*16 차원의 배열

arr = np.random.randint(0,10,(16,16))

# 4×4 블록마다 합 구하기
result = arr.reshape(4, 4, 4, 4).sum(axis=(1, 3))
# 원래는 2차원이었던 값을 
# reshape 하면서 axis가 0,1,2,3 으로 바뀌게 됨
# 이때 블럭 끼리 합하는게 아닌 블럭 안의 값을 더하고싶기에 
# axis = 1,3 만 설정해서 합하는것 


print(arr)
print("\n합:", result)

