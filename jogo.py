n = int(input())

pecas = 0
for i in range(n + 1):
    for j in range(i + 1):
        pecas += 1

print(pecas)
