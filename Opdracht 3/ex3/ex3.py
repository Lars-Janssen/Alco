import fileinput

invoer = []

for line in fileinput.input():
    invoer.append(line.split())

lengte = int(invoer[0][0]) + 1
goedAntwoord = invoer[0][1]

def Lengte(antwoord, juisteAntwoord):
    charArray = []
    m = len(antwoord)
    n = len(juisteAntwoord)
    for i in range(n + 1):
        charArray.append([0] * (m + 1))

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if antwoord[i - 1] == juisteAntwoord[j - 1]:
                charArray[i][j] = (charArray[i-1][j-1]) + 1
            else:
                charArray[i][j]= max(charArray[i][j-1], charArray[i-1][j])

    return charArray


def terugRekenen(charArray, antwoord, juisteAntwoord, i, j):
    if i == 0 or j == 0:
        return [""]
    if antwoord[i-1] == juisteAntwoord[j-1]:
        return [(z + antwoord[i-1]) for z in terugRekenen(charArray, antwoord, juisteAntwoord, i-1, j-1)]
    oplossingen = []
    if charArray[i][j-1] >= charArray[i-1][j]:
        oplossingen = oplossingen + terugRekenen(charArray, antwoord, juisteAntwoord, i, j-1)
    if charArray[i-1][j] >= charArray[i][j-1]:
        oplossingen = oplossingen + terugRekenen(charArray, antwoord, juisteAntwoord, i-1, j)

    return oplossingen


for i in range(1, lengte):
    antwoord = list(invoer[i][0])
    juisteAntwoord = list(goedAntwoord)
    m = len(antwoord)
    n = len(juisteAntwoord)
    antwoordArray = Lengte(antwoord, juisteAntwoord)
    print(str(antwoordArray[m][n]) + " " +  str(min(terugRekenen(antwoordArray, antwoord, juisteAntwoord, m, n))))