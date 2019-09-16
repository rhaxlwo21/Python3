import random

#선언
strPassword = ""
count= 0
randRange = 0
resultList = ""

#입력
strPassword = input("임시 비밀번호를 입력해 주세요 : ")
#print(strPassword) #입력을 받았는지 확인 / 확인하고 싶다면 print 앞에 # 제거
listPassword = list(strPassword)
#print(listPassword)        #비밀번호 배열 확인
count = int(len(listPassword)) - 1
#print(count)       #비밀번호 배열 개수 확인
#print(listPassword[count])     #배열의 특정 번호 출력

for i in range(0,count+1):
    print(listPassword[i])
    while True:
        a = random.randrange(33,127)
        print(a)
        if listPassword[i]==chr(a):
            break
    resultList = resultList + str(chr(a))

#결과출력
print("입력하신 비밀번호는 " + str(resultList))
