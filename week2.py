"""
1.  Write a Python program to get a list, sorted in increasing order by the last element in
each tuple from a given list of non-empty tuples. 


simple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


# sort 함수를 써서 사용 가능 -> sort 수 정렬 


# r = simple_list.sort(key=lambda x:x[1])
# # sort 는 정렬된값 반환도 안하고 무조건 none 을 반환하므로 
# # 변수지정, print 모두 안됨 
# print(r)\

simple_list.sort(key= lambda x: x[1])
print(simple_list)

# for 문 

result = []

while simple_list:

    small = simple_list[0]

    for x in simple_list:
        if x[1] < small[1]:
            small = x 

    result.append(small)
    simple_list.remove(small)

print(result)
"""

# Task 2. Given a string s1, write a program to return the sum and average of the digits that
# appear in the string, ignoring all other characters.
"""
x= input("given a string s1\n")

result=[]

for y in x: 
    if y.isdigit():
        result.append(int(y))

print("sum:", sum(result))
print("average:", sum(result)/len(result))

# map 함수를 이용해서 간단하게 사용 가능 
x = input("given a string\n")

result= list(map(int, filter(str.isdigit,x)))
print("sum:", sum(result))
print("sum:", sum(result)/len(result))


"""

"""
#Task 3. Write a Python program to sort a list of dictionaries using Lambda. 
# 순서 바꾸는 방법 

d = [{'make': ' Google ', 'model': 216, 'color': 'Black'}, 
{'make': 'MiMax', 'model': '2', 'color': 'Gold'},
# 1,2 번째 딕셔너리 순서 바꿈으로 새롭게 만들기 
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

d[1],d[2] = d[2],d[1]
print(d) 

# print - [{'make': ' Google ', 'model': 216, 'color': 'Black'}, 
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, 
# {'make': 'MiMax', 'model': '2', 'color': 'Gold'}]

"""

"""

# Task 4. Write a Python program to convert a given list of strings into 
# list of lists using map function.


given_list = ["abc", "def","ghi"]

new_list = list(map(list, given_list))
print(new_list)

"""

"""
# Task 5. Create a dictionary with the events in Dortmund and the date of the event. 
# List all events that were running during the Night of Museums in Dortmund on 19th September 2026


# 2026년 9월 주요 행사 및 일정 데이터 (전체 목록은 참조된 문헌에서 확인하실 수 있습니다)
events = {
    "Seebühne am Sonntag": "2026-09-06",
    "UEFA Champions League: BVB vs Villarreal CF": "2026-09-08",
    "Bundesliga: BVB vs SC Paderborn 07": "2026-09-12",
    "Autumn Opening Party at Laufsteg": "2026-09-12",
    "26th DEW21 Museum Night": "2026-09-19",
    "Seebühne am Sonntag (Season Finale)": "2026-09-20",
    "Dortmunder Oktoberfest": "2026-09-25 ~ 2026-10-17",
    "1st Philharmonic Concert: Seelenklaenge": "2026-09-30"
    
}


for events, date in events.items():
    if date == "2026-09-19":
        print(events)

"""

