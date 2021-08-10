import fileinput

a = []
for line in fileinput.input():
    a.append(line.split())

for i in range (2, len(a) + 1):
    n = len(a) - i
    for j in range (0, len(a[n])):
        a[n][j] = int(max(a[n+1][j], a[n+1][j+1])) + int(a[n][j])

print(a[0][0])