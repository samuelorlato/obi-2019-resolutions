n = int(input())
andares = input().split()

distancias = []
for i in range(n):
    for j in range(n):
        dist = i - j
        if dist < 0:
            dist = j - i

        distancias.append(int(andares[i]) + int(andares[j]) + dist)

distancias.sort()
print(distancias[-1])
