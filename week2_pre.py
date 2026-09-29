# week2 - python 
"""
# tuple - > {} 로 괄호로 print 됨 
my_tuple = (1, 2, 3,[4,5],"week2")
my_tuple[3][1] = 10 
# tuple 은 0부터 시작하고, 3번째 인덱스, 리스트의 1번째 인덱스 값을 10으로 바꿔줌
print(my_tuple)  # prints 5

print("number of elements in tuple: ", len(my_tuple))  
# 튜플의 길이를 출력할때
print("index number of 'week2':", my_tuple.index("week2"))
# 내가 원하는 튜플의 순서를 숫자로 나타낼때 
print("count of 1 in tuple: ", my_tuple.count(1))
# 찾는 튜플의 개수가 총 몇개인지 나타낼때 



# set - 쉽게 말해 집합으로 보면 됨 
my_set = {1,3}
y_set = {1,2,3,"chair"}

print(my_set)
my_set.add(2) # 하나의 원소만 추가가능 단, 컨테이너 자체를 넣기에 튜플로 입력이된다.   
print(my_set)
my_set.update([2,3,4])  # 여러개의 원소추가 가능 
print(my_set)
my_set.update([1,5],{1,6,8}) # update 는 컨테이너 자체를 넣는게 아닌, 안의 원소를 꺼내서 넣음
print(my_set)
my_set.add(("house",1)) # add 와 update 의 사용방법 
print(my_set)

print(y_set)
print(my_set&y_set) # 교집합 
print(my_set|y_set) # 합집합 
print(my_set-y_set) # 차집합
print(my_set^y_set) # 여집합  

"""

x = {'name': "stella", "age":20, "tall": 158}

# x.clear() 모든 값 삭제 
# x.copy() 모든 값 복제 
x2 = x.copy()
# 복제시 () 에는 인자 필요없음 이미 x 에 copy 했으므로
# 이때 x2 값을 바꾼다고 해도 원본에는 영향안줌 


# 새로운 딕셔너리 만들때 
new_keys = ["name",'age','tall'] #여러가지 key 생성가능
student = dict.fromkeys(new_keys) # 생성 후 dic 하나 생성해서 key 넣기 
student = dict.fromkeys(new_keys, "hello") # "" 로 value 값 지정가능


print(student)
# x의 value 값을 student 에 넣고싶다면? 
# for 문으로 해결해야함

student = { key : x[key] for key in new_keys}
# x[key] 를 불러내면 value 값이 나오기에 여기서 새로만든 리스트인 
# key 에는 new_keys 에서 불러들인 value 값들만 나오는것 ! 
print(student)

# key, value 불러오기
print(student.get('name'))
print(student.items())
print(student.keys())
print(student.values())

# 특정 key 삭제 
result = student.pop("tall")
print(result) # 삭제된 값이 저장된 value 가 되는것 
print(student) # dic 같이 불러야 빠진 값을 확인 가능 

result2 = student.popitem()
# popitem 제일 마지막 값 삭제 
print(student)

# setdefault() 
r = student.setdefault("name","kim")
print(r)
print(student)
r = student.setdefault("tall",158)
print(student)
# 원래 인자값이 있으면 추가 되지 않고, 새로운 값넣으면 추가됨. 반환값은 어쨌든 존재함.ㅣ
# 이때 update 를 넣어서 원래 값 변경 즉, 추가또는 변경 

r = student.update({"name":"jin"})
print(student)


# list-   순서 0, 값 변경 0 - 순서가 중요 나중에 변경필요할때
# tuple-  순서 0, 값 변경 x - 순서가 필요, 나중 변경 안됨 
# set -   순서 x, 값 변경 0 - 순서 필요, 중복이 필요없을때, 변경됨
# dic -   어떤 정보를 찾을때 - key 를 통해 value 를 찾음 


# lambda function : make simple function 
# map : apply the function to other various values

sqw = lambda i : i*i 
print(sqw(2))

pwp = lambda i,j : i*j
print(pwp(3,5))

l = [1,2,3,4,5]
print(list(map(lambda x : x*2,l)))

x_list= [1,5,4,6,8,11,3,12]
new_list = list(filter(lambda x: (x%2==0), x_list))
# filter 조건에 맞는 데이터만 골라낼때 쓰는 함수 

print(new_list)