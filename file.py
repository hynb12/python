file = open('a.txt', 'w')  # 'w' 덮어쓰기기
file.write('Hello, World')
file.close()

file = open('a.txt', 'a')  # 'a' 추가 append
file.write('\n반가워')     # 줄바꾸기 개행문자 '\n'
file.close()

file = open('a.txt', 'r')  # 'r' 읽기 read
print(file.read())

# csv파일(엑셀)
csvFile = open('data.csv', 'w')
csvFile.write('1,2,3'+'\n')
csvFile.write('4,5,6')

# 숙제1
리스트 = ['삼성전자', '카카오', '네이버', '신풍제약']

homework = open('homework.txt', 'w')
homework.write(리스트[0])
homework.write('\n'+리스트[1])
homework.write('\n'+리스트[2])
homework.write('\n'+리스트[3])
homework.close()
