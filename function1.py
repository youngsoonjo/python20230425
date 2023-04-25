#  function1.py
#1) 함수 정의
def times(a,b):
    return a*b

#2)함수 호출
result = times(3,4)
print(result)

def setValue(newValue):
    #지역변수
    x=newValue
    print("함수내부:", x)

#호출
retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x

#호출
print(swap(3,4))

def times(a=10,b=20):
    return a*b
print(times())
print(times(5))


# 디버깅 연습

def intersect(prelist, postlist):
    #교집합 문자를 모아둘 리스트 초기화(지역변수)
    result=[]
    #H(0) | A(1) | M(2)
    for x in prelist:
        #x라는 글자가 postlist에 있고, x가 아직 result에 없으면
        if x in postlist and x not in result:
            result.append(x)
    return result
    
#호출
print(intersect("HAM","SPAM"))

#지역변수와 전역변수
x=5 # 전연변수
def func(a):
    return x+a

#호출
print(func(1))

def func2(a):
    x=10 # 지역변수
    return x+a
#호출
print(func2(1))

#기본값
def times(a=10,b=20):
    return a*b
print(times())
print(times(5))
print(times(5,6))
# 선택한 행들을 주석처리: ctrl+/
# print(dir())

# 키워드 인자 방식(인자, 파라메터명을 상세하게 기술)
def connectURI(server,port):
    strURL = "http://"+server+":"+port
    return strURL

print(connectURI("credu.com","80"))
print(connectURI(port="8080",server="credu.com"))
print(globals())

g=lambda x,y:x*y
g(2,3)
