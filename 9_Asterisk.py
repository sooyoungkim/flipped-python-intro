############################################
# unpacking
############################################
data = ([1,2],[3,4],[5,6])
a,b,c = data
print(a, b, c)  # [1, 2] [3, 4] [5, 6]
print(*data)    # [1, 2] [3, 4] [5, 6]


for d in zip([1,2],[3,4],[5,6]) :
    print(d)
# (1, 3, 5)
# (2, 4, 6)

# unpacking 되면 zip([1,2],[3,4],[5,6]) 이 된다
for d in zip(*([1,2],[3,4],[5,6])) :
    print(d)
# (1, 3, 5)
# (2, 4, 6)

############################################
# Asterisk
#   - unpacking a container
#   - tuple, dict 등 자료형에 들어가 있는 값을 unpacking
#   - 함수의 입력값, zip등에 유용하게 사용가능
# *args
# **kwargs
############################################
def asterisk_test1(a, *args): # tuple로 packing
    print(a, args)
    print(args[0])
    print(type(args))

def asterisk_test2(a, args):
    print(a, *args)           # unpacking
    print(type(args))

def asterisk_test3(a, b, c, d):
    print(a,b,c,d)


asterisk_test1(1, *(2,3,4,5,6)) # *(2,3,4,5,6)이 unpacking 되어 2,3,4,5,6 으로 들어간다.
# 1 (2, 3, 4, 5, 6)
# 2
# <class 'tuple'>

asterisk_test1(1, (2,3,4,5,6)) # tuple 값인 (2,3,4,5,6)이 들어간다.
# 1 ((2, 3, 4, 5, 6),)
# (2, 3, 4, 5, 6)
# <class 'tuple'>

asterisk_test2(1, (2,3,4,5,6))
# 1 2 3 4 5 6
# <class 'tuple'>


ex = {"b": 1, "c": 2, "d": 3}
asterisk_test3(10, **ex)    # unpacking 되어 b=1, c=2, d=3으로 들어간다.
# 10 1 2 3

ex = {"b": 1, "c": 2, "e": 3}
asterisk_test3(10, **ex)
# TypeError: asterisk_test3() got an unexpected keyword argument 'e'
