import numpy as np 

"""
print("nunmpy_versoion", np.__version__)

# 1 dimensional array
data = [10,20,30]
arr = np.array(data)
print("first dimensional array", arr)
print("type of array", type(arr))
print("1.shape= {} , size={} dtype={}, ndim={}".format(arr.shape, arr.size, arr.dtype, arr.ndim))
# ndim = 배열이 몇 차원인지 알려주는 속성
# 내려가는방향아 axis = 0 
# 옆 방향이 axis = 1

data2 = [[1,2,3],[4,5,6]]
print("2 dimensional array", data2)
arr2 = np.array(data2, dtype=float)
print("2.shape= {} , size={} dtype={}, ndim={}".format(arr2.shape, arr2.size, arr2.dtype, arr2.ndim))


data3 = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
print("3 dimensional array", data3)
arr3 = np.array(data3, dtype=float)
print("3.shape= {} , size={} dtype={}, ndim={}".format(arr3.shape, arr3.size, arr3.dtype, arr3.ndim))
                                                       
"""

arr = np.arange(10)
np.info(arr)
print(arr)

arr = np.zeros((3,4), dtype=int)
print(arr)

arr= np.ones((3,4), dtype=int)
print(arr)

arr= np.full((3,4), 3, dtype=int)
print("last:\n",arr)

arr = np.empty(3) # 저 크기의 배열생성 단 초기화는 x
print(arr) # 출력해보면 원래 가지고있는 값이 나옴 
# unlikely np.zeros() -> 원하는 배열을 생성 후 초기화 

data = [[1,2,3],[4,5,6]]
sample = np.array(data)
arr = np.ones_like(sample) # sample과 같은 shape의 배열을 생성 후 1로 초기화
print(arr)

print(np.arange( 0, 2, 0.3 ) )
