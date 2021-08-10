import fileinput
invoer  = []

for line in fileinput.input():
    invoer.append(line.split())

leerlingen = int(invoer[0][0])
scripties = int(invoer[0][1])
graaf = []

for i in range(leerlingen):
    graaf.append([0] * scripties)

for i in range(1, len(invoer)):
    leerling = int(invoer[i][0]) - 1
    scriptie = int(invoer[i][1]) - 1
    graaf[leerling][scriptie] = 1

def berekenpad(leerling, bezet, bekeken):
        for scriptie in range(scripties):
            if(graaf[leerling][scriptie] == 1 and bekeken[scriptie] == False):
                bekeken[scriptie] = True
                if(bezet[scriptie] == -1 or berekenpad(bezet[scriptie], bezet, bekeken) == True):
                    bezet[scriptie] = leerling
                    return True
        return False

def maximum():
    bezet = [-1] * scripties
    resultaat = 0
    for i in range(leerlingen):
        bekeken = [False] * scripties
        if(berekenpad(i, bezet, bekeken) == True):
            resultaat += 1
    return resultaat

print(maximum())
