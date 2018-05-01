############################################################
# 사용자가 서버에 입력한 명령어를 기록한 로그를 활용 -> command, id 형태
# 어떤 사용자가 명령어를 얼마나 많이 입력했을까?
############################################################
import csv

def getKey(item):		# 정렬을 위한 함수
    return item[1]

command_data = []		# 파일 읽어오기
with open("resources/command_data.csv", "r", encoding="utf8") as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='"') # Object
     for row in spamreader:
        command_data.append(row)

# 결과) ['python3.4 submit_assignment.py -submit gowithflow.py', 'tiana']
print(command_data[3])

command_counter = {} 			# dict 생성, 아이디를 key값, 입력한 명령어 수를 value값
for data in command_data:		# list 데이터를 하나씩 가져오기
    if data[1] in command_counter.keys(): 	# 아이디가 이미 Key값으로 변경되었을 때
        command_counter[data[1]] += 1		# 기존에 나온 아이디이면 + 1
    else:
        command_counter[data[1]] = 1		# 처음 나온 아이디이면 1로 초기화

dictlist = []
for key, value in command_counter.items():
    temp = [key,value]
    dictlist.append(temp)


sorted_dict= sorted(dictlist, key=getKey, reverse=True) # list를 입력 줄 수로 (내림차순)정렬
print (sorted_dict[:100])			# List의 상위 100개 값만 출력
