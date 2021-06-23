ONSET_START_LETTER = 4352
NUCLEUS_START_LETTER = 4449
CODA_START_LETTER = 4520

JAMO_START_LETTER = 44032
JAMO_END_LETTER = 55203
JAMO_CYCLE = 588

import codecs

def isHangul(ch): #한글인지 아닌지
    JAMO_START_LETTER = 44032
    JAMO_END_LETTER = 55203
    return ord(ch) >= JAMO_START_LETTER and ord(ch) <= JAMO_END_LETTER

def getOnset(ch): #초성 추출
    return chr(int(((ord(ch) - JAMO_START_LETTER) / 28) / 21 + ONSET_START_LETTER))

def getNucleus(ch): #중성 추출
    return chr(int(((ord(ch) - JAMO_START_LETTER) / 28) % 21 + NUCLEUS_START_LETTER))

def getCoda(ch): #종성 추출
    return chr(int((ord(ch) - JAMO_START_LETTER) % 28 + CODA_START_LETTER -1))


k = 0

a = str(input("문자를 입력 : "))
if len(a) > 1:
    for i in range(0, len(a)-1):
        if ord(getCoda(a[i])) == 4527 and ord(getOnset(a[i+1])) == 4354:
            print(getCoda(a[i])+"과",getOnset(a[i+1])+"에서","유음화 현상 일어남")
        if ord(getCoda(a[i])) == 4523 and ord(getOnset(a[i+1])) == 4357:
            print(getCoda(a[i])+"과",getOnset(a[i+1])+"에서","유음화 현상 일어남")
        if ord(getCoda(a[i])) == 4546:
            k = k + 1
        if ord(getOnset(a[i+1])) == 4370:
            k = k + 2
        if k == 1 and ord(getOnset(a[i+1])) == 4352: 
            print(getCoda(a[i])+"과",getOnset(a[i+1])+"에서","자음 축약 현상 일어남")
        if k == 1 and ord(getOnset(a[i+1])) == 4355:
            print(getCoda(a[i])+"과",getOnset(a[i+1])+"에서","자음 축약 현상 일어남")
        if k == 1 and ord(getOnset(a[i+1])) == 4359:
            print(getCoda(a[i])+"과",getOnset(a[i+1])+"에서","자음 축약 현상 일어남")
        if k == 1 and ord(getOnset(a[i+1])) == 4364:
            print(getCoda(a[i])+"과",getOnset(a[i+1])+"에서","자음 축약 현상 일어남") #까지 ㅎ이 종성
        if k == 2 and ord(getCoda(a[i+1])) == 4520:
            print(getCoda(a[i])+"과",getOnset(a[i+1])+"에서","자음 축약 현상 일어남")
        if k == 2 and ord(getCoda(a[i+1])) == 4526:
            print(getCoda(a[i])+"과",getOnset(a[i+1])+"에서","자음 축약 현상 일어남")
        if k == 2 and ord(getCoda(a[i+1])) == 4536:
            print(getCoda(a[i])+"과",getOnset(a[i+1])+"에서","자음 축약 현상 일어남")
        if k == 2 and ord(getCoda(a[i+1])) == 4541:
            print(getCoda(a[i])+"과",getOnset(a[i+1])+"에서","자음 축약 현상 일어남")
