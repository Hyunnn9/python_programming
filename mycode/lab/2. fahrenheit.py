"""
섭씨를 화씨로 변환하기
화씨 = 9/5 * 섭씨온도 + 32
"""

#섭씨를 화씨로 변환하는 함수
def fah_convert(celsuis):
    return ((9/5) * float(celsuis)) + 32

print("섭씨온도 입력요망")
user_input = input()
print(type(user_input), user_input)
fah = fah_convert(user_input)

print('섭씨온도 :' , float(user_input))
print(f'섭씨온도 : {user_input}')
# 포멧 생략하기
print('화씨온도 : {0:.f}'.format(fah))
print(f'화씨온도 : {round(fah,2)}')
# 포멧 생략하고 소수둘째 자리에서 반올림하기
# format(fah,str)