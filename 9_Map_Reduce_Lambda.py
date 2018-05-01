###############################################################
# Lambda
#   - 간단한 코드로 다양한 기능을 제공하지만 코드의 직관성이 떨어지는 면이 있다.
#   - python3+ 많이 사용되지 않는다. def function으로 구현하는 것을 권장
#   - List Comprehension 을 사용한다.
###############################################################
###############################################################
# Map
#   - sequence 자료형 각 element 에 동일한 function을 적용해준다.
#   - map(function_name, list_data1, list_data2,...)
#   - Map 대신 List Comprehension 으로 많이 사용한다.
###############################################################
data1 = [1,2,3,4,5]
f = lambda x: x ** 2

# map 결과 자체는 아직 generater 상태이다.
#       즉, 메모리만 생성만 해둔 상태이다.
#       실행 시점에 값이 정해진다.
#       list()로 묶어주면 (실행) -> list로 사용가능
import sys
sys.getsizeof(data1)                # 104
sys.getsizeof(map(f, data1))        #  56
sys.getsizeof(list(map(f, data1)))  # 128
print(map(f, data1))                # <map object at 0x104744b00>
print(list(map(f, data1)))          # [1, 4, 9, 16, 25]

# lambda 의 경우 if filter 추가하면 반드시 else를 넣어주어야한다.
result2 = list(map(lambda x: x ** 3 if x % 2 == 0 else x, data1))
print(result2)          # [1, 8, 3, 64, 5]


data2 = [5,4,3,2,1]
result3 = list(map(lambda x, y: x + y, data, data2))
print(result3)          # [6, 6, 6, 6, 6]

# zip을 사용한 것과 동일한 결과가 출력된다.
#       zip만 실행하면 아직 generator 상태
#       for문 (실행) -> 값을 사용가능
print(zip(data1, data2)) # <zip object at 0x1046e9208>
result4 = []
for x,y in zip(data1, data2):
    result4.append(x + y)
print(result4)          # [6, 6, 6, 6, 6]


###############################################################
# Reduce
#   - 동일한 function을 적용해서 sequence 자료형 각 element를 통합한다.
###############################################################
from functools import reduce

data11 = [1,2,3,4,5]

# 1+2=3 -> 3+3=6 -> 6+4=10 -> 10+5=15
print(reduce(lambda x, y: x + y, data11))   # 15

def factorial(n):
    return reduce(
        lambda x, y: x * y, range(1, n+1)
    )

# n=5 -> range(1, 6) -> 1*2=2 -> 2*3=6 -> 6*4=24 -> 24*5=120
factorial(5)    # 120
