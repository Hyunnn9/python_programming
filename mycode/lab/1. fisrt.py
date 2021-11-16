"""
멀티라인 주석은 이렇게 한다.
한줄짜리는 샵으로 하면 된다.
숏컷은 아래와 같다
ctrl + shft + f10 = run
ctrl + / : line comment
"""

def add(n1,n2):
    #pass
    return n1 + n2
print(type(add))
print(add(10,20))

#ctrl + shift + f10 실행

add2 = lambda n1,n2 : n1 + n2
print(type(add2))
print(add2(100,200))


#class 선언
class User:
        # 생성자 선언
        def __init__(self, name):
            self.name = name
    # toString()
        def __str__(self):
            return self.name

# 객체 생성
user = User("파이썬")
print(user)
print(type(user))