# DemoSetTuple.py

print("---SET형식---")
a={1,2,3,3}
b={3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("---tuple형식---")
tp=(1,2,3)
print(type(tp))


# 함수 정의
def calc(a,b):
    return a+b, a*b

print(calc(3,4))


print("id: %s, name:%s" %("kim","김유신") )
args=(5,6)
print(calc(*args))