# -*- coding: utf-8 -*- 
"""
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


numbers = [-7,4,-3,6,3,-8,3,4]
#numbers = [-7,4,-3,6]

numberSize = len(numbers)
maxSum = 0
for i in range(0,numberSize):
    for j in range(i,numberSize):
        pSum = 0
        for k in range(i,j):
            pSum += numbers[k]
        if pSum > maxSum:
            maxSum = pSum
#print(maxSum)

#재귀호출 
def findMaxSum(numArr, start, end):
    if start == end:
        return numArr[start]

    mid = (start+end)/2
    print(start)
    print(end)
    print(mid)
    
    leftMaxSum = -27810394
    numSum = 0
    for i in range(mid, start-1, -1):
        print("leftNum :: " + str(numArr[i]))
        numSum += numArr[i]
        #print("leftMaxNum :: " + str(leftMaxSum))
        print("numSum :: " + str(numSum))
        leftMaxSum = max(leftMaxSum, numSum)
        print("leftMaxSum ::" + str(leftMaxSum))

    rightMaxSum = -27810394
    numSum = 0
    for j in range(mid+1, end+1):
        numSum += numArr[j]
        print("rightNum :: " + str(numArr[j]))
        #print("rightMaxNum :: " + str(rightMaxSum))
        print("numSum :: " + str(numSum))
        rightMaxSum = max(rightMaxSum, numSum)
        print("rightMaxSum ::" + str(rightMaxSum))

    #print("fun::" + str(findMaxSum(numArr, start, mid)))
    #return max(findMaxSum(numArr, start, mid), 0)
    findMaxSum(numArr, mid+1, end)
    singleSum = max(findMaxSum(numArr, start, mid), findMaxSum(numArr, mid+1, end))
    print("singleSum :: " + str(singleSum))
    return max(leftMaxSum + rightMaxSum, singleSum)

print(findMaxSum(numbers,0,numberSize-1))

'''
- range의 다른방법, 2차배열 생성, 리스트 append 사용, bool 조건 not 

팀 해본적 없는 사람끼리 2명 1개조로 구성 할 수 있는 경우의 수
'''
 
MEMBER_CNT = 4

#팀 해본 적 없는 팀원을 2차배열로 선언 
isTeamList = [[False]*4 for i in range(4)]
isTeamList[0][1] = True
isTeamList[0][2] = True
isTeamList[0][3] = True
isTeamList[1][2] = True
isTeamList[1][3] = True
isTeamList[2][3] = True


def findTeam(pHasTeam):
    #팀원번호가 작은 순서부터 차례대로 탐색 할 수 있도록 firstMember를 선언
    firstMember = -1
    print(pHasTeam)

    #멤버 중 번호가 가장 작고 팀에 속하지 않은 팀원을 추출
    for i in range(MEMBER_CNT):
        if not pHasTeam[i]:
            firstMember = i
            print("firstMember ::" + str(firstMember))
            break

    #추출할 팀원이 더 이상 없을 경우 1번의 갯수 반환
    if firstMember == -1:
        return 1

    totCnt = 0
    for secondMember in range(firstMember+1, MEMBER_CNT):
        #가장 작은 번호의 멤버와 그 다음 번호의 멤버를 조건에 대입 
        if not pHasTeam[firstMember] and not pHasTeam[secondMember] and isTeamList[firstMember][secondMember]:
            #조건에 맞을 경우 
            pHasTeam[firstMember] = True
            pHasTeam[secondMember] = True
            print("member f :: " + str(firstMember))
            print("member s :: " + str(secondMember))
            #조건에 맞는 멤버를 제외하고 나머지 멤버에 대해서 재귀함수 반복 
            totCnt += findTeam(pHasTeam)
            pHasTeam[firstMember] = False
            pHasTeam[secondMember] = False
            print("totCnt  :: " + str(totCnt))
    return totCnt


#hasTeam 배열 
hasTeam = []
for i in range(4):
    hasTeam.append(False)
#실행 
findTeam(hasTeam)

boardType = [[[0 for i in range(2)] for j in range(3)] for k in range(4)]
boardType[0] = [[0,0],[1,0],[0,1]]
boardType[1] = [[0,0],[1,0],[1,1]]
boardType[2] = [[0,0],[0,1],[1,1]]
boardType[3] = [[0,0],[0,1],[-1,1]]

board = [[0 for i in range(6)] for j in range(2)]
#board[1][0] = 1


def set(board, typeNum, firstX, firstY, delta):
    isWellDone = True
    if delta == -1:
        print("=========================치우기start ============================")
    print("typeNum :: " + str(typeNum))
    for j in range(3):
        typeX = firstX + boardType[typeNum][j][0]
        typeY = firstY + boardType[typeNum][j][1]
        if delta != -1:
            print("type X :" + str(typeX))
            print("type Y :" + str(typeY))
            #print(pBoard[typeY][typeX])
        
        #블록의 위치가 board에서 벗어나는 경우 False 반환
        if typeY < 0 or typeX < 0 or typeY >= len(board) or typeX >= len(board[0]):
            print("isWellDone 1")
            isWellDone = False
        #delta 값(1,-1)에 따라서 블록을 채울지 삭제할지 결정
        else:
            board[typeY][typeX] += delta
            #해당 자리에 이미 블록이 존재하는 경우 False 반환 
            if board[typeY][typeX] > 1:
                print("isWellDone 2")
                isWellDone = False
    print(board[0])
    print(board[1])
    if delta == -1:
        print("=========================치우기end ============================")
    return isWellDone

def makeBoard(pBoard):
    print(pBoard)
    firstX = -1
    firstY = -1
    
    #3개짜리 도형이기때문에 3의 배수가 아닌 경우 전부 채울 수 가 없습니다.
    #3으로 나눠서 나머지가 0이 아닌경우는 제외 합니다.
    if len(pBoard) % 3 != 0:
        print("블록의 크기가 3의 배수가 아닙니다.") 
        return -1
    
    #첫번째 시작점 선택(가장 왼쪽 위로부터 시작)
    for i in range(len(pBoard)):
        for j in range(len(pBoard[i])):    
            if 0 == pBoard[i][j]:
                firstY = i
                firstX = j
                break
        if firstY != -1:
            break
    
    print("첫번째 X 좌표 :: " + str(firstX))
    print("첫번째 Y 좌표 :: " + str(firstY))

    #반복문이 끝났음에도 -1일 경우 더이상 남은 칸이 없는 것으로 판단 
    if firstX == -1:
        return 1
    ret = 0  
    #type별로 반복 탐색 
    for i in range(4):
        result = False

        #해당 블록 타입이 맞지 않을 경우 False  반환 
        result =  set(pBoard, i, firstX, firstY, 1)
        
        print(result)
        
        #해당 블록 타입이 맞을 경우 재귀함수 호출하여 오른쪽 아래 순으로 계속 탐색 
        if result:
            ret += makeBoard(pBoard)
        
        #모든 탐색이 끝났으면 탐색 이전 블록타입 삭제 
        set(pBoard, i, firstX, firstY, -1)

    
    print(pBoard[0])
    print(pBoard[1])
    print("ret :: " + str(ret))
    return ret

#    for i in range(
#test
#board[0][0] = 1
makeBoard(board)


dots = [1,0,0,0]
dists = [[0 for i in range(4)] for j in range(4)]
dists[0][1] = 3
dists[0][2] = 4
dists[0][3] = 1
dists[1][2] = 3
dists[1][3] = 1
dists[2][3] = 1

def setDots(pDots, startDot, distSum, minDistSum):

    if 0 not in dots:
        distSum += dists[0][startDot]
        minDistSum = min(minDistSum, distSum)

        print("distSum :: " + str(distSum))
        print("minDistSum :: " + str(minDistSum))
        return minDistSum

    ret = 0

    for i in range(1, len(pDots)):
        if pDots[i] == 0:
            pDots[i] = 1
            print(pDots)
            if dists[startDot][i] ==0:
                distSum += dists[i][startDot]
            else:
                distSum += dists[startDot][i]

            print("distSum ::" + str(distSum))
            print("minDistSum1 :: " + str(minDistSum))
            print("startDot :: " + str(startDot))
            print("endDot :: " + str(i))

            minDistSum = setDots(pDots,i,distSum,minDistSum)
            pDots[i] = 0
            distSum -= dists[startDot][i]

    print(minDistSum)
    return minDistSum
setDots(dots,0, 0, 38902309)


dots = [1,0,0,0]

def setDots(pDots):
    if 0 not in dots:
        return 1

    ret = 0
    for i in range(1, len(pDots)):
        if pDots[i] == 0:
            pDots[i] = 1
            ret += setDots(pDots)
            pDots[i] = 0

        print(ret)
    return ret
setDots(dots)
"""

#times = [12,12,12,12,12,12]

switches = [[0,1,5],[0,1,2,5],[0,1,2,3,5]]
def makeTime(isSwitch, times, ret, clickCnt):
    
    tweleveCnt = 0
    for i in times: ## java: Arraylist.contains(item)
        if i == 12:
            tweleveCnt+=1

    if tweleveCnt == len(times):
        print("complete")
        return clickCnt
    
    for j in range(len(switches)):
        if isSwitch[j] == 0:
            isSwitch[j] = 1
            print(isSwitch)
            print(times)
            print("click switch")
            clickCnt += 1
             
            for k in switches[j]:
                print(switches[j])
                if times[k] == 12:
                    times[k] = 3
                else:
                    times[k] += 3
                print(times)
            ret = makeTime(isSwitch, times, ret, clickCnt)
            print("ret :: " + str(ret))
            isSwitch[j] = 0
        if ret > 0:
            print(ret)
            return ret

    return -1

pTimes = [3,3,6,9,12,3]
pisSwitch = [0,0,0]

makeTime(pisSwitch, pTimes, 0, 0)
