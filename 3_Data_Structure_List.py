############################################
# list의 값들을 잘라서 쓰는 것이 slicing
# slicing 사용방법
#       [start(include), end(exclude), step]
############################################
cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '성남', '순천', '수원']
print(type(cities))

# ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '성남', '순천', '수원']
#    0     1      2       3      4      5     6      7      8      9
#  -10    -9     -8      -7     -6     -5    -4     -3     -2     -1
#
# [0:6] 0 ~ 5까지
# [-9:] -9부터 끝까지
print("[0:6] ", cities[0:6])
print("[-9:] ", cities[-9:])
#
# 콜론 : 처음부터 끝까지
# 범위를 넘어갈 경우 자동으로 최대 범위를 지정
print("[:] ", cities[:])
print("[-50:50] ", cities[-50:50])
#
# [::2] 2칸 단위로
# [::-1] 역으로 1칸 단위로
print("[::2]", cities[::2])
print("[::-1]", cities[::-1])

cities[9] = "제주"
print("제주" in cities)

############################################
# 추가 & 삭제
############################################
colors1 = ['red', 'blue', 'green']
colors2 = ['grey', 'black', 'white']

# 추가 : colors1 자제가 바뀐다.
colors1.append("+orange")
print(colors1)
colors1.extend(colors2)
print(colors1)
colors1.insert(1, "+white")
print(colors1)

# 삭제 : colors1 자제가 바뀐다.
del colors1[1]
print(colors1)
colors1.remove("+orange")
print(colors1)

############################################
# Python 리스트만의 특징들
############################################
# 다양한 Data Type이 하나의 List에 들어감
a = ["colors", 55, 0.2]
print(a)
# 리스트 안에 리스트 넣기 가능
a[0] = colors2
print(a)
# 행렬형태의 리스트
kor = [20, 40, 60, 80]
math =[12, 23, 34, 45]
eng = [98, 87, 76, 65]
midtern = [kor, math, eng]
print(midtern[1][3])
# 언패킹 : 한 변수의 데이터를 각각의 변수로 반환
t1, t2, t3 = a
print(t1, t2, t3)
