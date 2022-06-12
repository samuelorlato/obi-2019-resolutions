m = int(input())

f1 = int(input())
f2 = int(input())

f3 = m - (f1 + f2)

fs = [f1, f2, f3]
fs.sort()

print(fs[-1])
