############################################
# Call by Object reference
############################################
def spam(eggs) :
    # Local
    eggs.append(1)  # 기존 리스트에 원소 추가
    print("1. ham :", ham)
    print("1. eggs:", eggs)

    eggs = [2,3]    # 리스트 새로 할당하고 그 주소를 eggs에 대입
    print("2. ham :", ham)
    print("2. eggs:", eggs)

# Global
# ham 할당
ham = [0]
print("before ham :", ham)
# before ham : [0]

# ham 주소를 parameter eggs에 대입(같은 곳을 가리킨다.)
spam(ham)
print("after ham :", ham)
# 1. ham : [0, 1]
# 1. eggs: [0, 1]
# 2. ham : [0, 1]
# 2. eggs: [2, 3]
# after ham : [0, 1]


############################################
# 가변인자 매개변수
############################################
# asterisk(*) 한 개(*) 사용 -> tuple type으로 들어간다.
print("===== asterisk 한 개(*) 사용해보기 =====")
def asterisk_test(a, b, *args):
    #print(type(args))   # <class 'tuple'>
    print("a: ", a, ", b: ", b, ", args: ", args)
    print("a + b + sum(args) = ", a + b + sum(args))

    x, y, *z = args # unpacking은 3개 항목까지만 가능, z에 나머지 모두 넣는다
    return x, y, z

print(asterisk_test(3,4,5))
# a:  3 , b:  4 , args:  (5,)
# a + b + sum(args) =  12
# ValueError: not enough values to unpack (expected at least 2, got 1)
print("unpacking: ", asterisk_test(3,4,5,6))
# a:  3 , b:  4 , args:  (5, 6)
# a + b + sum(args) =  18
# unpacking:  (5, 6, [])
print("unpacking: ", asterisk_test(1,2,3,4,5))
# a:  1 , b:  2 , args:  (3, 4, 5)
# a + b + sum(args) =  15
# unpacking:  (3, 4, [5])
print("unpacking: ", asterisk_test(1,2,3,4,5,6,7))


# asterisk(*) 두 개(**) 사용 -> dict type(key와 value로 구성)으로 들어간다.
print("===== asterisk 두 개(**) 사용해보기 =====")
def double_asterisk_test(**kwargs) :
    print("kwargs: ", kwargs)
    print("First value is {first}".format(**kwargs))
    print("Second value is {}".format(kwargs["second"]))

double_asterisk_test(first=3, second=4, third=5)


print("===== asterisk 한 개(*)와 두 개(**) 모두 사용해보기 =====")
def kwargs_test(one, two, *args, **kwargs) :
    print("one: ", one, ", two : ", two, ", args: ", args, ", kwargs: ", kwargs)
    print(one + two + sum(args))

kwargs_test(3,4,5,6,7,8,9, first=3, second=4, third=5)
