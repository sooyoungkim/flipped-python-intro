############################################
# 조건
############################################
# birth_year = int(input("당신이 태어난 년도를 입력하세요 : "))
#
# age = (2018 - birth_year) + 1
#
# if(20 <= age <= 26):  # if 26 <= age and age >= 20
#     print("대학생")
# elif(17 <= age < 20): # elif age < 20 and age >= 17
#     print("고등학생")
# elif(14 <= age < 17): # elif age < 17 and age >= 14
#     print("중학생")
# elif(8 <= age < 14):  # elif age < 14 and >= 8
#     print("초등학생")
# else:
#     print("학생이 아닙니다.")

############################################
# 반복
############################################
# (1) multiplication table
# multiplication = int(input("구구단 몇 단을 계산할까요? (1~9): "))
#
# while (multiplication != 0) :
#     if(multiplication < 10 and multiplication > 0) :
#         print("구구단 {}단을 계산합니다.".format(multiplication))
#         for i in range(1,10):
#             print("{0:2d} X {1:2d} = {2:2d}".format(multiplication, i, multiplication * i))
#         multiplication = int(input("구구단 몇 단을 계산할까요? (1~9): "))
#     else:
#         multiplication = int(input("잘못입력하셨습니다. 1~9단만 가능합니다 : "))
# print("구구단을 종료합니다.")


# (2) reverse
# sentence = "I Love You"
# reverse_sentence =  ''
# for char in sentence:
#     reverse_sentence = char + reverse_sentence
# print(sentence, "-- [reverse] ->", reverse_sentence)


# (3) decimal number to binary number
# decimal = 10
# result = ''
# print("------------------------------")
# print("remainder ", " | ", " decimal")
# print("------------------------------")
# while (decimal > 0):
#     remainder = decimal % 2  # 나머지
#     decimal = decimal // 2    # 몫
#     print("{0:11d} | {1:10d}".format(remainder, decimal))
#     result = str(remainder) + result
#
# print("2진수로 변환 : ", result)


# (4) 숫자 찾기 게임
# import random
# guess_number = random.randint(1, 100)
#
# # is not : 메모리 주소 비교, == : 값 비교
# user_number = int(input("숫자를 맞춰보세요(1~100) : "))
# while (user_number is not guess_number):
#     if user_number > guess_number :
#         print("숫자가 너무 큽니다.")
#     else :
#         print("숫자가 너무 작습니다.")
#
#     user_number = int(input("다시 도전 : "))
#
# print("정답입니다. 숫자는 {} 입니다.".format(user_number))


# (5) 학생별 평균
#           A |  B  |  C  |  D  |  E
# =====================================
# 국어점수   49    79    20   100    80
# 수학점수   43    59    85    30    90
# 영어점수   49    79    48    60   100
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

# 과목 수
subjects = len(midterm_score)
# 학생 수
students = len(midterm_score[0])

# 학생 별 평균
student_avg = []
for i in range(students) :
    total = 0
    for j in range(subjects) :
        total += midterm_score[j][i]

    student_avg.append( total // subjects )

print("학생별 평균 : ", student_avg)
