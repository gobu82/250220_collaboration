# 천하제일 코드 자랑
# 파이썬 코드를 자랑해주세요

print("안녕하세요")

for row in range(5):
    for col in range(5):
        if col == 0:
            print("*", end = "")

        elif col <= 2 and row > 0 and row <= 3:
            print("*", end = "")

        elif col <= 4 and row > 1 and row < 3:
            print("*", end = "")

    print()
