import fileinput

givenInput = []
distanceGraph = []

for line in fileinput.input():
    # line bevat al een newline van zichzelf
    givenInput.append(line.split())

cities = int(givenInput[0][0])

for i in range(0, cities):
    distanceGraph.append([1000] * cities)

for i in range(1, len(givenInput)):
    cityA = int(givenInput[i][0])
    cityB = int(givenInput[i][1])
    distance = int(givenInput[i][2])
    distanceGraph[cityA][cityB] = distance
    distanceGraph[cityB][cityA] = distance

visited = [0]
nextCity = 0
cheapestRoute = 0
while(len(visited) != cities):
    cheapest = 1000
    for i in visited:
        for j in range(0, cities):
            if(distanceGraph[i][j] < cheapest and j not in visited):
                cheapest = distanceGraph[i][j]
                nextCity = j
    visited.append(nextCity)
    cheapestRoute += cheapest

print(cheapestRoute)