# 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오.
# 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.
# 점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.


x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)
