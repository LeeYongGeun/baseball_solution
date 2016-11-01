import random
DIGITMAX = 3
k = 0
a=1
def get_number(n,digit):     #자릿수를 표현하는 함수
    k= (n//(10**(digit-1)))%10
    return k
def n_digit(n):             # 몇자린지 말해주는 함수
    a=1
    while n>10:
            n//=10
            a+=1
    return a
print(get_number(987654321,8))
print(n_digit(123456))


rn = random.randint(0,999)
while get_number(rn,1) == get_number(rn,2)or get_number(rn,2) == get_number(rn,3) or get_number(rn,3) == get_number(rn,1):
    rn = random.randint(0,999)
print(rn)
while True:
    ans = None
    try :
        ans = int(input("Input:"))
    except :
        continue

    if ans<0 or ans>999:
        continue

    strike = 0
    ball = 0
    for i in range(DIGITMAX):
        for j in range(DIGITMAX):
            if i == j and get_number(rn, i+1) == get_number(ans, j+1):
                strike += 1
            if i !=j and get_number(rn, i+1) == get_number(ans, j+1):
                ball += 1
    print (strike, ball)
    if strike == DIGITMAX:
        break

