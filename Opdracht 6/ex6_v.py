import fileinput
import sys
invoer = []
for line in fileinput.input():
    invoer.append(line.split())


if(invoer[0][0] + " "+ invoer[0][1] == "Niet vervulbaar"):
    print("Niet vervulbaar")
    sys.exit()

aantal_var = int(invoer[0][0])
aantal_conj = int(invoer[0][1])

variables = []


for i in range(1, aantal_var + 1):
    for j in range(0,2):
        variables.append(invoer[i][j])

conjuctions = []
for i in range(aantal_var + 1, len(invoer)):
    conjuctions.append(invoer[i])


for i in range(len(conjuctions)):
    conj_variables = []
    for j in range(len(conjuctions[i])):
        active_conj = conjuctions[i][j]
        if("~" in active_conj):
            active_conj = active_conj[1:len(active_conj)]
            active_variable = active_conj
            var = variables[variables.index(active_variable) + 1]
            if(int(var) == 0):
                var = "1"
            else:
                var = "0"
            conj_variables.append(var)
        else:
            active_variable = active_conj
            conj_variables.append(variables[variables.index(active_variable) + 1])

    if( "1" in conj_variables):
        continue
    else:
        print(variables)
        print(conjuctions)
        print("Vervult formule niet")
        sys.exit()

print("Vervult formule")