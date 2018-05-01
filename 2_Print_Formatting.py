# 출력 포매팅 방법들
d = 1
e = 2
f = 3

print(d,e,f)    # (1) 콤마 : 실행 시 두 문장 연결, 한칸 띄우고 출력됨
print("%d %d %d" % (d,e,f))       # (2) %-format
print("{} {} {}".format(d,e,f))   # (3) str.format()

# 패딩 적용
day = 5
product = "Apple"
price = 5.243
print("Date : %2d일 -> Product: %10s, Price per unit: %5.2f"
        % (day, product, price))

print("Date : {0:2d}일 -> Product: {1:>10s}, Price per unit: {2:5.2f}"
        .format(day, product, price))

print("product ID : {0:5d}, Price : ${1:8.2f}".format(453, 59.058))
print("product ID : {0:5d}, Price : ${1:.5f}".format(453, 59.058))
