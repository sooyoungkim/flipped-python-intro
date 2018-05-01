f = open("resources/yesterday.txt", 'r')
yesterday_lyric = ""
while 1 :
    line = f.readline()
    if not line :
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"

f.close()

# 대소문자 구분없이 yesterday 단어의 개수 세기 : 대문자로 또는 소문자로 만들고 카운드 세기
num_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")
print("Number of a Word 'YESTERDAY'", num_of_yesterday)

# 대소문자 구분하여 Yesterday 와 yesterday의 개수를 세보자.
num_of_small_yesterday = yesterday_lyric.count("yesterday")
num_of_title_yesterday = yesterday_lyric.count("Yesterday")
print("Number of a Word 'yesterday'", num_of_small_yesterday)
print("Number of a Word 'Yesterday'", num_of_title_yesterday)
