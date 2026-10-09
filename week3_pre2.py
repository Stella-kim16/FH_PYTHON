import pandas as pd 


# series 속성 - 1차원 데이터 
"""
year = [2010, 2011, 2012, 2013, 2014]
result = pd.Series(year)

print(result) # 0부터 인덱스 시작됨 
print()
print(type(result))


print(result.index)
print(result.values)
print(result.dtype)
print(result.shape)

print()

result.name='year'
result.index.name = 'No'
print(result)

year = [2019,2020,2021,2022]
idx = ['A','B','C','D']
result= pd.Series(data = year, index = idx, name = 'year')
print(result)
print()


# 딕셔너리 데이터로 series 생성 - 한번에 지정할거면 딕셔너리 
# 아니면 리스트로 data 랑 index 값 각각 넣기 
score = {'A': 90, 'B': 80, 'C': 70}
result = pd.Series(data = score, name = 'score')
print(result)   
print()

"""

"""
# dataframe 속성 - 2차원 표 형식의 데이터 

score = {'name': ['Kim', 'lee', 'park'], 
          'score':[100,90,50],
          'grade':["A","B","C"]}


dp = pd.DataFrame(data = score)
print(dp)
print(type(dp))
print()

print(dp.index)
print(dp.columns)
print(dp.values)

print(dp.dtypes)
print(dp.shape)
print()

score = {'name': ['Kim', 'lee', 'park','chio'] ,
          'score':[100,90,50,40],
          'grade':["A","B","C","D"]}

i  = ['a','b','c','d']
c = ['score', 'grafe','name','email']

dp = pd.DataFrame(data = score, index = i , columns= c )
print(dp)
print()

score =  {'name': ['Jessi', 'Emma', 'Alex', 'idan', 'Tom'],
         'score': [100, 95, 80, 85, 97],
         'grade': ['A', 'A', 'B', 'B', 'A'],
         'subject':['python', 'java', 'python', 'c', 'java']}


score_df = pd.DataFrame(data =score)
print(score_df)

print(score_df.info())
print(score_df.head(5))
print(score_df.tail(3))
print()

# 예시 샘플을 뽑는 함수 
print("random_Sample:", score_df.sample())
print()

# n 수를 정해서 샘플 뽑기 
print("고정 샘플값:", score_df.sample(2,random_state=10))

# 비율로 샘플뽑는법 5개중 20% 이면 1/5 니까 하나만 출력 되도록 
print("비율 샘플값 :", score_df.sample(frac=0.2))

"""

# 수치형과 범주형 데이터 
"""

score = {'name': ['Jessi', 'Emma', 'Alex', 'Jessi', 'Tom'],
         'age': [20, 24, 23, 20, 27],
         'score': [100, 95, 80, 85, 100],
         'grade': ['A', 'A', 'B', 'B', 'A'],
         'subject':['python', 'java', 'python', 'c', 'java']}

result = pd.DataFrame(data = score )

# print(result.head(3))

# print(result.describe())

print(result[['age','name']].count())
# count 는 df 함수라서 꼭 [[]] 로 사용 - 행렬을 불러오는것이므로 
# count 행과 열에서 결측치가 아닌 값을 불러오는 것 
print(result["age"].unique())
# unique 는 1차원 데이터 값을 불러오는것이므로 - [ ] 만 사용 
# 중복을 제거한 고유한 값 반환 
print("3",result["score"].mode())
# 최빈값을 불러올때 사용, [ ] 사용
# 이떄 최빈값의 index 도 같이 나옴, ex- 0 100 이렇게
# 100 이 가장 최빈값이며 100의 인덱스 숫자인 0 도 같이 출력됨 
print(result["score"].mode()[0]) 
# 슬라이싱으로 인덱스 없이 출력도 가능 
print(result["subject"].value_counts(normalize=True))
# 각 값이 몇번등장했는지 확인할때 [] 사용 동일 

"""

"""
# 데이터 조회 및 변경 

score = {'name': ['Jessi', 'Emma', 'Alex', 'Jessi', 'Tom'],
         'score': [100, 95, 80, 85, 97],
         'grade': ['A', 'A', 'B', 'B', 'A'],
         'subject':['python', 'java', 'python', 'c', 'java']}
c = ['name', 'subject', 'score', 'grade', 'etc']


dp = pd.DataFrame(data = score, columns= c)
print()


print(dp.name)
# print(dp['name']) 도 가능 

print(dp[["name", "score","grade"]])
# key,value 모두 가져오려면 [[ ]] 를 사용해야하는것 잊지말기 !

# 0 값 처리
dp['etc'] =0
print(dp) 
print()

print("ex:",dp.loc[3])# 원하는 행값 불러오기 - loc 를 사용해서 
print(dp.loc[[2,3]]) # 다중 데이터 불러오기 - 2차행렬이므로 [[]]


dp.loc[0] = ['Jessi', 'java', 70, 'C', 1]
print("new:\n", dp)


# 기존의 데이터를 가지고 선택후 새로운 dp 를 만드는 방법 
row_idx = [1,2,4]
col_idx = ['name','subject','grade']
print(dp.loc[row_idx,col_idx])

"""

"""
# 데이터 추가 및 삭제 
score = {'name': ['Jessi', 'Emma', 'Alex', 'Jessi', 'Tom'],
         'score': [100, 95, 80, 85, 97],
         'grade': ['A', 'A', 'B', 'B', 'A'],
         'subject':['python', 'java', 'python', 'c', 'java']}
c = ['name', 'subject', 'score', 'grade', 'etc']
df = pd.DataFrame(data=score, columns=c)
# print(df)


# 새로운 col 추가 및 내용 
semester_data  = pd.Series(['20-01', '20-01', '20-02', '20-01'])
df["semester"] = semester_data
# print(df)

# 비교 연산자를 이용한 새 col 추가 
df["high_score"] = df["score"]> 90
# print(df)

df.loc[5] = ['Jina', 'python', 100, 'A', 1, '20-02', True]
# print(df)

# 행삭제 
df.drop(5) 
# print(df)

#원본까지 삭제하고 싶을때 
df.drop(5, inplace = True)
# print(df)

#행을 삭제하고 싶을때는 - 결측치가 너무 많거나 필요없을때 
df.drop(columns= ['etc'], inplace = True)
print(df)

"""
"""
# CSV 파일 읽어오기 

file =pd.read_csv('Cars93_missing.csv')
# print(file.head(3))

# print(file.columns)

# 결측치 처리 
df = pd.DataFrame(data= file)
print(df)

print(df.info())
print(df.isnull().sum()) # 각 컬럼별 결측값의 개수 확인
print(df.isnull().sum(axis=1)) # 각 행별 결측값 개수 확인도 가능 

"""
import numpy as np
"""
# 결측치 처리 


df = pd.DataFrame(data = np.arange(18).reshape(6,3),
				  index = ['a','b','c','d','e','f'],
                  columns=['col1','col2','col3'])

df['col4'] = pd.Series(data = [1.7, 1.2, 2.4], 
                       index = ['a','e','c'])

df.loc['c'] = None
# print(df.info())
# 5non-null 뜻 - > 5개의 정상적인 값이 있다 
# print(df.isnull().sum()) # 행 기준
# print()
# print(df.isnull().sum(axis=1)) # 열 기준 

# 행이 all 결측치인 값만 삭제하고 원본에도 반영 
print(df.dropna(how = "all", inplace=  True))

print(df.dropna(axis=1, inplace = True))

print(df)

"""

"""

# 슬라이싱  

d = {'name': ['Jessi', 'Emma', 'Alex', 'Jessi', 'Tom'],
     'score': [100, 95, 80, 85, 97],
     'grade': ['A', 'A', 'B', 'B', 'A'],
     'subject':['python', 'java', 'python', 'c', 'java']}

sample_df = pd.DataFrame(data=d)
# coloum 값 index 로 변환법 
sample_df.set_index('name', inplace=True)

# print(sample_df)

print("slicing:", sample_df[1:4])
print()
print("second", sample_df[:2])
print()
print(sample_df[:"Alex"])
print()
print(sample_df.iloc[:4 , -1]) # 행열 둘다 슬라이싱 가능 iloc 를 쓰면
                  
"""

"""
# 집계함수 


score = {'sub1': [3, 9, 1, 1, 9],
         'sub2': [2, 9, np.nan, np.nan, 8],
         'sub3': [np.nan, 1, 5, 5, 7],
         'sub4': [np.nan, 3, np.nan, 1, np.nan]}

dp = pd.DataFrame(data = score)
print(dp)
print()
print("axis 0 기준 \n",dp.count()) 
# 기준을 토대로 각 열에 몇개의 데이터가 있는지 - 결측값빼고 알려줌 
print()
print("1 기준\n",dp.count(axis=1))
# 1이므로 행에 몇개의데이터가 존재하는지 
#print(df.sum(skipna=False)) - 결측값까지 포함하고 싶을때

result =  pd.concat([df2,df1,df3],ignore_index = True) 
# sum 과 다른점 
# 숫자 데이터를 합치는 sum 과 다르게 
# concat 은 2개의 df 의 표를 연결하는것 

"""
"""
# 데이터 그룹화 

sample = {'product':['a','b','a','b','a','b','a','a'],
          'sensor':['s1','s1','s2','s3','s2','s2','s1','s3'],
          'x':np.arange(1,9),
          'y':np.arange(5,13)}

df = pd.DataFrame(data=sample)
print(df)

list_ = df.groupby("product")
print(list)

# for key, value in list_:
#     print(key)
#     print(value) # 보면 product 기준으로 나눠진거 확인

print(list_.sum())
# print(list_)

# 2개 이상으로 그룹화 
# list2 = df.groupby(['product','sensor']).sum()

list3 = df.groupby(["product",'sensor'])['x'].sum()
# product, sensor 그룹 화 이후에 x 들만 다시 또 집합시키기 
print("list3:\n",list3)
list4 = df.groupby(["product",'sensor']).sum()
print("list4:\n",list4)
# 여기는 x로 안묶었기 때문에 x,y 값 모두 보여줌 

# function= {'x':'max', 'y':'min'}
 # 조건은 딕셔너리로 정의 : 적용함수를 딕셔너리로 정의 - 중요!!
list5 =  df.groupby(['product', 'sensor']).agg(
    max = ('x','max'),
    min = ('y', "min"))

print("5:\n",list5)

"""