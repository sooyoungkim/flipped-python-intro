# Java 나 C와 코드 스타일이 다르다.
# 많은 개발자들이 사용하는 python 스타일로 코딩하면
# 다른 사람의 코드에 대한 이해도도 높아지고
# 내 코드에 대한 다른 사람의 이해도도 높아진다.


########################################################
# Zip
#   - 두 개의 List를 병렬로 처리하는 것
########################################################
a,b,c = zip((1,2,3), (10,20,30), (100,200,300))
print(a,b,c)
# (1, 10, 100) (2, 20, 200) (3, 30, 300)

total = [sum(x) for x in zip((1,2,3), (10,20,30), (100,200,300))]
print(total)
# [111, 222, 333]

for i, (a,b) in enumerate(zip(['tic', 'tac', 'toe'], ['a1', 'a2', 'a3'])):
    print(i,a,b)
# 0 tic a1
# 1 tac a2
# 2 toe a3


########################################################
# Enumerate
#   - List의 element를 추출할 때 index 번호를 붙여서 추출
########################################################
# list의 index와 value를 unpacking
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)
# 0 tic
# 1 tac
# 2 toe

# list로 변경 ([])
print(list(enumerate(['tic', 'tac', 'toe'])))
# [(0, 'tic'), (1, 'tac'), (2, 'toe')]

# dict로 변경({key:value})
print({i:v for i, v in enumerate("Let's see the highlights from the lighting ceremony for the Olympic".split())})
# {0: "Let's", 1: 'see', 2: 'the', 3: 'highlights', 4: 'from', 5: 'the', 6: 'lighting', 7: 'ceremony', 8: 'for', 9: 'the', 10: 'Olympic'}


########################################################
# 중요!!!!!
# List Comprehension
#   - 기존 List를 사용하여 간단히 다른 새로운 List를 만드는 기법
#   - 포괄적인 List, 포함되는 List 라는 의미
#   - 파이썬에서 가장 많이 사용되는 기법 중 하나
#   - 일반적으로 for loop + append 보다 속도가 빠르다.
########################################################
# 기존 list
result = []
for i in range(10):
    result.append(i)
print(result)

# list comprehension
result_comprehension = [i for i in range(10)]
print(result_comprehension) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#   아래 구문을 한 줄에 표현 가능하다
#   result_comprehension_filter = []
#   for i in range(10):
#       if (i % 2 == 0)):
#           result_comprehension_filter.append(i)
result_comprehension_filter = [i for i in range(10) if i % 2 == 0]
print(result_comprehension_filter)  # [0, 2, 4, 6, 8]


world_1 = "hi"
world_2 = "world"

# One dimensional 로 만들기
#   아래 구문을 한 줄에 표현 가능하다
#   worlds = []
#   for i in world_1:
#       for j in world_2:
#           if not (i == j):    # i랑 j가 같다면 List에 추가하지 않는 필터링 추가
#               worlds.append(i+j)
worlds = [i+j for i in world_1 for j in world_2 if not (i == j)]
print(worlds)
# ['hw', 'ho', 'hr', 'hl', 'hd', 'iw', 'io', 'ir', 'il', 'id']


# Two dimensional 로 만들기 - 1
text = "The quick brown fox jumps over the lazy dog".split()
words = [[w.upper(), w.lower(), len(w)] for w in text]
print(words)
# [['THE', 'the', 3],
#   ['QUICK', 'quick', 5],
#   ['BROWN', 'brown', 5],
#   ['FOX', 'fox', 3],
#   ['JUMPS', 'jumps', 5],
#   ['OVER', 'over', 4],
#   ['THE', 'the', 3],
#   ['LAZY', 'lazy', 4],
#   ['DOG', 'dog', 3]]


# Two dimensional 로 만들기 - 2
#   아래 구문을 한 줄에 표현 가능하다
#   worlds = []
#   for j in world_2:
#       for i in world_1:
#           worlds.append(i+j)
worlds_ = [[i+j for i in world_1] for j in world_2]
print(worlds_)
# [['hw', 'iw'],
#   ['ho', 'io'],
#   ['hr', 'ir'],
#   ['hl', 'il'],
#   ['hd', 'id']]


# Two dimensional 을 One dimensional 로 변경하기
#   아래 구문을 한 줄에 표현 가능하다
#   one = []
#   for x in words:
#       for word in x:
#           one.append(word)
one = [word for x in words for word in x]
print(one)
['THE', 'the', 3, 'QUICK', 'quick', 5, 'BROWN', 'brown', 5, 'FOX', 'fox', 3, 'JUMPS', 'jumps', 5, 'OVER', 'over', 4, 'THE', 'the', 3, 'LAZY', 'lazy', 4, 'DOG', 'dog', 3]


########################################################
# for loop 대신 stirng 에서는 join과 split을 많이 사용하도록 하자.
########################################################

########################################################
# Join
########################################################
colors = ["www","theteamlab","io"]
print("".join(colors))
print("-".join(colors))


########################################################
# Split
########################################################
items = 'zero one two three'.split() # 빈칸 기준으로 문자열 나누기
print(items)

example = "www.theteamlab.io"
subdomain, domain, tld = example.split(".")
print(subdomain, domain, tld)
