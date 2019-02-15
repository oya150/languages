# -*- coding: utf-8 -*- 
#출력
#print("Hello World!")

#변수 출력
num = 1
name = "KimSungHyun"
#print(num)
#print(name)

#문자열 반복
#print(name * 2) #결과: KimSungHyunKimSungHyun
#print("=" * 10) #결과: ==========


##반복문 조건문
##주어진 문자열에서 가장 많은 빈도수를 가진 문자 출력하기 
mihs = ['m','a','d','e','i','n','h','e','a','v','e','n']
alphabets = [chr(i) for i in range(97,123)]
#print(alphabets)

'''
#정렬 라이브러리 사용
mihs.sort() #timesort algorithm java에서는 7부터 배열정렬은 quicksort list정렬은 timesort

print(mihs)

#1.중복 루프
maxAlphabet = ''
maxAlphabetCnt = 0
alphabetCnt = 0

for alphabet in alphabets:
    alphabetCnt = 0

    for mih in mihs:
        if mih==alphabet:
            alphabetCnt += 1

    if alphabetCnt > maxAlphabetCnt:
        maxAlphabetCnt = alphabetCnt
        maxAlphabet = alphabet

print(maxAlphabet)
'''

#2.딕셔너리 이용(빠름빠름)
dicMih = {}

for mih in mihs:
    dicMih[mih] = 0

#print(dicMih)

mihCnt = 0
maxMihCnt = 0
maxMih = ''
for mih in mihs:
    # if mih in mihs 를 사용하면 상단 루프문 안써도 됨  
    dicMih[mih] += 1
    
    if dicMih[mih] > mihCnt:
        mihCnt = dicMih[mih]
        maxMih = mih

#print(dicMih)
#print(maxMih)

'''
- 반복문(range, 증가,감소), 배열사이즈
- 숫자를 문자 타입으로 변경(str():소수점 한자리 까지 ,repr():소수점 그대로 변환 ) 

주어진점수배열(1년간 월별 점수)에서 3개월 단위로 평균점수 출력하기  
'''
scores = [3,2,4,6,2,1,3,5,4,8,4,3]
averSize = 3
scoreSize = len(scores)
startNum = averSize-1

#중복루프 이용 
for i in range(startNum, scoreSize):
    average = 0
    sumVal = 0
    for j in range(i,i-averSize, -1):
        sumVal += scores[j]
        
    #print(str(i+1) + ' 월평균 :: ' + str(sumVal/averSize))


#단일루프 이용 
sumScore = 0
for i in range(0, averSize):
    #print(scores[i])
    sumScore += scores[i]
    #print(sumScore)

firstNum = 0
for j in range(startNum, scoreSize, 1):
    #print(str(j+1) + ' 월평균 :: ' + str(sumScore/averSize))
    if j != scoreSize-1:
        sumScore -= scores[firstNum]
        sumScore += scores[j+1]
        firstNum += 1


numbers = [-7,4,-3,6,3,-8,3,4,]

numberSize = len(numbers)
maxSum = 0
for i in range(0,numberSize):
    for j in range(i,numberSize):
        pSum = 0
        for k in range(i,j):
            pSum += numbers[k]
        if pSum > maxSum:
            maxSum = pSum
print(maxSum)

