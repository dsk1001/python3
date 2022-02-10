# while문
num = 1
while num <= 100: # num가 100 이하일 때 까지 반복
    print(num)
    num = num + 1 # 한 번 반복 될 때마다 num를 1씩 증가


# continue
# 조건에 따라 while문을 빠져나갈 수도 있지만, 맨 처음으로(조건문)으로 다시 돌아가고 싶을 때 사용한다.
# 예제 - 1부터 10까지의 숫자 중에서 홀수만 출력
a = 0
while a < 10:
    a = a+1
    if a % 2 == 0: continue # a가 짝수인 경우 조건문으로 돌아가 다시 수행
    print(a)


# break
# while문을 강제로 빠져나가고 싶을 때 사용한다.
# 예제 - 커피 자판기
"""
커피 자판기에서 커피가 몇 개 남았는지 보여주고, 커피가 다 소진되었다면 break하는 구문을 작성 해보자.
"""
coffee = 10
money = 500
while money:
    print("돈을 받았습니다. 커피를 제공합니다.")
    coffee = coffee-1
    print("커피가 현재 10개 중 %d개 남았습니다." % coffee)
    if coffee == 0:
        print("커피가 전부 소진 되었습니다.")
        break
# 예제 - 커피 자판기 (심화)
"""
위의 예제에서 금액을 따로 입력 받아서 커피를 제공해주자.
거스름 돈 계산도 넣자.
"""
coffee1 = 3
print("커피 한 잔의 값은 500원입니다.")
while True:
    money1 = int(input("돈을 넣어주세요: "))
    if money1 == 500:
        coffee1 = coffee1-1
        print("커피를 제공 해드립니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee1)
    elif money1 >= 500:
        coffee1 = coffee1-1
        print("커피를 제공 해드립니다. 거스름돈은 %d원 입니다." %(money1-500))
        print("남은 커피의 양은 %d개 입니다." % coffee1)
    else:
        print("금액이 모자랍니다. 돈을 돌려주고 커피를 주지 않습니다.")
    if coffee1 == 0:
        print("커피가 모두 소진되었습니다. 판매를 중지합니다.")
        break


# 무한 루프
while True:
    print("Ctrl + c를 입력해야 빠져나갈 수 있습니다.")