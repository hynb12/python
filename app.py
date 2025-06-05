리스트 = ['삼성전자', '카카오', '네이버', '신풍제약']

homework = open('homework.txt', 'w')
homework.write(리스트[0])
homework.write('\n'+리스트[1])
homework.write('\n'+리스트[2])
homework.write('\n'+리스트[3])
homework.close()
