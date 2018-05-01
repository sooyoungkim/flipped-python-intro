############################################
# 콘솔 창 입력
############################################
somebody = input("이름을 입력하세요 : ")
print("Hi " + somebody + "!" )

# 입력시 바로 형변환
#   콘솔창 입력 값은 string 타입 -> float으로 형변환해서 사용한다.
# temperature = float(input("온도를 입력하세요 : "))
# print(temperature)

# 섭씨를 화씨로 변환
celsius = float( input("변환하고 싶은 섭씨 온도를 입력해주세요 : ") )
fahrenheit = ((9/5) * celsius) + 32

print("섭씨온도 : ", celsius)
print("화씨온도 : ", format(fahrenheit, '.1f'))
print("화씨온도 : ", "{0:.1f}".format(fahrenheit))
