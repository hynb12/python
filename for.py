사셈 = ['BMW사셈', 'K5사셈', '스파크사셈']

for i in 사셈:
    print(i + '!!!')

# 숙제1
리스트 = ['삼성전자', '카카오', '네이버', '신풍제약']

homework = open('homework_for.txt', 'w')

for i in range(4):
    homework.write(리스트[i]+'\n')

homework.close()

# 숙제2 구구단, str()은 숫자에 따옴표쳐주는 문법
for i in range(2, 10):
    for j in range(1, 10):
        print(str(i) + ' x ' + str(j) + ' = ' + str(i*j))
