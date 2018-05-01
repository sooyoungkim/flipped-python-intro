import sys
print(sys.getsizeof("a"))   #50 Bytes -> 49(기본) + 1(a)
print(sys.getsizeof("ab"))  #51 Bytes -> 49 + 1(a) + 1(b)
print(sys.getsizeof("abc")) #52 Bytes -> 49 + 1(a) + 1(b) + 1(c)
print("--------------------")
str = "TEAMLAB"
str2 = "teamlab"
str3 = "we learn P YTHON "

print(str[3:5])
print(str[::-1])

print(str * 2)
print("A" in str)
print("G" in str)
print(len(str))

print(str.lower())
print(str2.upper())
print(str.capitalize())  # 첫 글자만 대문자로 변환
print(str2.capitalize()) # 첫 글자만 대문자로 변환
print("str3.capitalize() : ", str3.capitalize()) # 맨 앞 단어의 첫 글자만 대문자로 변환
print("str3.title() : ", str3.title())           # 띄어쓰기된 각 단어마다 첫 글자는 대분자로 변환
print("str3.find('rn') : ", str3.find("rn"))
print("str3.startswith('we')", str3.startswith("we"))
print("str3.endswith('hon')", str3.endswith("hon"))
print("str3.count('n') : ", str3.count('n'))
print("str3.count('N') : ", str3.count('N'))
print("str3.index('r') : ", str3.index('r'))
print("str3.split(' ')", str3.split(' '))
print(str3.strip())   # 문장 맨앞/맨뒤의 공백 제거 (모두 공백 X)

print("55".isdigit())
print("It's OK")
print('It\'s OK')
print(""" It's OK.
        It's Good.
        \\See you.
""")

########################################################
# slicing 더 확인해보기
########################################################
# print(a[0:6])    # a 변수의 0~5 까지
# print(a[-9:])    # a 변수의 -9부터 끝까지
# print(a[:])      # a 변수의 처음부터 끝까지
# print(a[-50:50]) # 범위를 넘어갈 경우 자동으로 최대 범위를 지정
# print(a[::2])    # a 변수를 2칸 단위로
# print(a[::-1])   # a 변수를 역으로 1칸 단위로
