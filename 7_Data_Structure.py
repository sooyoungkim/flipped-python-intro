########################################################
# namedtuple
#   - tuple형태로 데이터 속성에 대한 'Data 구조체'' 저장
#       - class 는 데이터 속성 + 행동을 정의할 수 있다.
#   - 저장되는 data의 variable을 사전에 지정해서 저장
########################################################
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y']) # 이름, 컬럼명리스트

p = Point(11, y=22)
print(p[0] + p[1])
print(p.x + p.y)

x, y = p
print(x, y)

########################################################
# counter
#   - data type들의 data elemet들의 갯수를 dict 형태로 반환
#   - element() / subtract()
########################################################
# from collections import Counter
#
# c = Counter()           # a new, emtpy Counter
# c = Counter('gallahad') # a new counter from an iterable
# print(c)
#
# c = Counter({'red': 4, 'blue': 2})
# print(c)                  # Counter({'red': 4, 'blue': 2})
# print(list(c.elements())) # ['red', 'red', 'red', 'red', 'blue', 'blue']
#
# c = Counter(a=4, b=2, c=0, d=-2)
# d = Counter(a=1, b=2, c=3, d=4)
# print(c-d)  # Counter({'a': 3})
# print(c)    # Counter({'a': 4, 'b': 2, 'c': 0, 'd': -2})
# print(d)    # Counter({'d': 4, 'c': 3, 'b': 2, 'a': 1})
#
# # c 값 차제가 변경
# c.subtract(d)
# print(c)    # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})


########################################################
# defaultDict
#   - Dict와 달리, 데이터를 입력한 순서대로 dict를 반환함
#   - 신규 값 생성시 해당 key가 존재하지 않을 경우 value에 기본값을 지정해서 생성한다
#   - Reference from https://dongyeopblog.wordpress.com/2016/04/08/python-defaultdict-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0/
#   - Text-mining 접근법 - Vector Space Model 에 유용
#       - 하나의 지문에 각 단어들이 몇 개나 있는지 세고 싶을 경우
########################################################
# from collections import defaultdict
# from collections import OrderedDict
#
# # d = defaultdict(object)   # Default dictionary를 생성 (생성자)
# d = defaultdict(lambda: 1)  # Default 값을 1로 설정합
# print(d["first"])           # 1 이 출력


########################################################
# orderedDict
#   - Dict와 달리, 데이터를 입력한 순서대로 dict를 반환함
########################################################
# from collections import OrderedDict
#
# print("데이터를 임의대로 dict로 반환함")
# d = {}
# d['x'] = 100
# d['y'] = 200
# d['z'] = 300
# d['l'] = 500
# for k, v in d.items():
#     print(k, v)
#
# print("데이터를 입력한 순서대로 dict로 반환함")
# od = OrderedDict()
# od['x'] = 100
# od['y'] = 200
# od['z'] = 300
# od['l'] = 500
# for k, v in od.items():
#     print(k, v)
#
# print("key를 기준으로 오름차순 정렬")
# for k, v in OrderedDict(sorted(d.items(),
#                         key=lambda t: t[0])).items():
#                         print(k, v)
#
# print("value를 기준으로 내림차순(역순으로) 정렬")
# for k, v in OrderedDict(sorted(d.items(),
#                         reverse=True,
#                         key=lambda t: t[1])).items():
#                         print(k, v)


########################################################
# deque
#   - stack (LIFO)과 queue(FIFO)를 지원하는 모듈
#   - 양방향  Linked List의 특성을 지원
#   - list 보다 효울적인 메모리 구조로 처리속도 향상
#   - list에 비해 효율적인 자료 저장 방식을 지원함
#   - append() / appendleft() / rotate() / reverse() / extend() / extendleft()
########################################################
# from collections import deque
# deque_list = deque([0, 1, 2, 3, 4, 5])
#
# deque_list.appendleft(10)
# print(deque_list)   # deque([10, 0, 1, 2, 3, 4, 5])
# deque_list.rotate(2)
# deque_list.appendleft([7,5,7])
# print(deque_list)   # deque([[7, 5, 7], 4, 5, 10, 0, 1, 2, 3])


########################################################
# 여기서 부터는 기본 테이터 타입들입니다.
########################################################

########################################################
# dictionary (dict 타입)
#   - 값을 순서 없이 저장, 임의대로 dict를 반환함
#   - key와 value를 매칭하여 사용
#   - {1997: "서인국", 1994: "정우", 1988: "박보검"}
#   - items() / keys() / values()
########################################################
# response_series = {1997: "서인국", 1994: "정우", 1988: "박보검"}
# print(response_series.keys())
# print(response_series.values())
#
# def compare_value(dict, value) :
#     for k,v in dict.items():
#         if(v == value):
#             return k;
#
# print("응답하라 {}".format(compare_value(response_series, "박보검")))


########################################################
# tuple
#   - 값의 변경만 제외하면 list 에서 할 수 있는 것은 모두 할 수 있다.
#   - 값의 변경이 불가능한 리스트
#       - 변경 불가한 값을 저장하는데 유용하다. (예, 학번 , 주민번호, 우편번호 등)
#   - 값이 하나인 tuple은 반드시 ","를 붙여야한다.
#   - (1,2,3,4,5)
########################################################
# print(type((1)))  # <class 'int'>
# print(type((1,))) # <class 'tuple'>


########################################################
# set
#   - 값을 순서없이 저장
#   - 중복 불허
#   - add() / remove() / update() / discard() / clear() / union() 합집합(|) / intersection() 교집합(&) / difference() 차집합(-)
#   - {1,2,3,4,5}
########################################################


########################################################
# stack
#   - Last In First Out (LIFO) : 나중에 넣은 데이터를 먼저 반환
#   - push / pop
#   - append() / pop()
########################################################
# word = input("Input a word: ")
#
# # string을 list로 변환
# # "Hello, Sooy"
# #   -> ['y', 'o', 'o', 'S', ' ', ',', 'o', 'l', 'l', 'e', 'H']
# word_list = list(word)
#
# result = []
# # 사용하지 않는 변수에 _ 사용 가능
# for _ in range(len(word_list)):
#     result.append(word_list.pop())
#
# print("".join(result))
# print(word[::-1])


########################################################
# queue
#   - First In Fist Out : 먼저 넣은 데이터를 먼저 반환
#   - put / get
#   - append() / pop(0)
########################################################
