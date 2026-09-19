## Numeric types - int, float, complex
# x/y quotient(몫) of x and y -> 
# x//y floored(내림) quotient of x and y
# x % y remainder(나머지만 출력) of x and y
# abs() absolute value of x (절댓값)
# complex(real, imag(복소수) complex number with real and imag parts
# c.conjugate() complex conjugate of c (복소수의 켤레복소수반환[-])
# divmod(x, y) quotient and remainder of x and y (몫과 나머지 반환) 
# pow(x, y) x raised to the power y (x의 y승) 

"""
x = 10
y = 2.4
print("1. value: " , x/y )
print("2. value: " , x//y )
print("3. value: " , x%y )
""" 

# Bitwise operators
# x & y bitwise AND of x and y (비트단위 AND)
# x | y bitwise OR of x and y (비트단위 OR) - 둘중 하나라도 1이면 1
# not(x|y) bitwise NOR of x and y (비트단위 NOR) - OR의 반대값
# x ^ y bitwise XOR of x and y (비트단위 XOR) - 두값이 서로 다를때 1
# x << n left shift of x by n bits (x를 n비트 왼쪽으로 이동)
# x >> n right shift of x by n bits (x를 n비트 오른쪽 
# x ~ n bitwise NOT of x (x의 비트단위 NOT)-입력된 비트의 반대값을 반환


# 10진법 수를 2진법수로 바꾸는 방법 
# 오른쪽 -> 왼쪽으로 읽으면서 8,4,2,1 로 생각 
# 5 는 1010 이 되고 13은 1101 3은 0011 15는 1111
# 출력값은 10진수로 다시 나오기 때문에 2진수로 받고싶으면 bin() 함수를 사용해야함


'''
a,b = 13,15
print("4. value: " , a&b ) 
print("4. value: " , bin(a&b)) 


# string 
# single quote 
print('Hello "World"') # allows embedded "" quotes
# double quote
print("Hello World")   
# triple quote

print("""first line    # allows to span multiple lines
second line
third line""")

print("""
she said, \n"what a wonderful day!"
""")

'''
# 리스트비교시 첫번째 원소만 보고 true/ false 인지 결과 도출 
list1= [1,2,3,4]
list2=[5,6,7]

print(list1 <list2) 