b = int(input())
t = int(input())

AREA = 70 * 160

area = (b + t) * 70 / 2
area_resto = AREA - area

if area > area_resto:
    print(1)
elif area < area_resto:
    print(2)
else:
    print(0)
