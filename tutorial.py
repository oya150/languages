# -*- coding: utf-8 -*- 
#출력
print("Hello World!")

#변수 출력
num = 1
name = "KimSungHyun"
print(num)
print(name)

#문자열 반복
print(name * 2) #KimSungHyunKimSungHyun
print("=" * 10) #==========


##반복문 조건문
mihs = ['m','a','d','e','i','n','h','e','a','v','e','n']
alphabets = [chr(i) for i in range(97,123)]
print(alphabets)

#정렬

print(mihs)
      
'''
maxAlphabet = ''
maxAlphabetCnt = 0
mihCnt = 0
for mih in mihs:
    print(alphabet)
    mihCnt = 0
    for alphabet in alphabets:
        if mih==alphabet:
'''

#정렬 라이브러리 사용
mihs.sort() #timesort algorithm

