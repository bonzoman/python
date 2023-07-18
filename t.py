startNo, endNo = 0, 102
for i in range(startNo, endNo):  # 1부터 100까지의 숫자를 반복
    if i == startNo or i % 10 == 0:
        print("현재 숫자는", i, "입니다.")

# 마지막에 한 번 더 실행하는 코드
if not i % 10 == 0:
    print("코드 실행이 종료되었습니다.", i)
