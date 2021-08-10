import fileinput
import sys
import math
import os

invoer = []
for line in fileinput.input():
    invoer.append(line.split())

aantal_var = int(invoer[0][0])
aantal_conj = int(invoer[0][1])
vervulbaar = False


combinaties = []
tijdelijke_invoer = []
for i in range(0, int(math.pow(2, aantal_var))):
    tijdelijke_invoer = invoer
    combinaties.append(bin(i))
    combinaties[i] = combinaties[i].replace("0b", "")
    while(len(combinaties[i]) < aantal_var):
        combinaties[i] = "0" + combinaties[i]

    for j in range(0, aantal_var):
        var = combinaties[i]
        tijdelijke_invoer[j+1].append(var[j])


    variables = []
    for i in range(1, aantal_var + 1):
        for j in range(0,2):
            variables.append(tijdelijke_invoer[i][j])

    conjuctions = []
    for i in range(aantal_var + 1, len(tijdelijke_invoer)):
        conjuctions.append(tijdelijke_invoer[i])

    voldoet = True
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
            voldoet = False

    if(voldoet == True):
        #Bron: https://stackoverflow.com/questions/45027681/pythonic-way-to-print-2d-list-python
        print('\n'.join(map(' '.join, tijdelijke_invoer)))
        vervulbaar = True
        break


    for j in range(0, aantal_var):
        del(tijdelijke_invoer[j+1][1])

if(vervulbaar == False):
    print("Niet vervulbaar")
