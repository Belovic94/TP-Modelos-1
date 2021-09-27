def main():
    combinations = []
    times = {}
    incompabilities = {}
    clothes = 0
    file = open('enunciado.txt', 'r')
    for line in file:
        row = line.split()
        if row[0] == 'p':
            clothes = int(row[2])
        elif row[0] == 'e':
            if (row[1] in incompabilities):
                incompabilities[row[1]].append(row[2])
            else:
                incompabilities[row[1]] = [row[2]]
        elif row[0] == 'n':
            times[row[1]] = int(row[2])
    for i in range(1, clothes + 1):
        firstIndex = str(i)
        for j in range(1, clothes + 1):
            secondIndex = str(j)
            if ( firstIndex != secondIndex and secondIndex not in incompabilities[firstIndex]):
                time = times[firstIndex] if times[firstIndex] > times[secondIndex] else times[secondIndex]
                combinations.append((firstIndex, secondIndex, time))
    orderedCombinations = sorted(combinations, key=lambda x: x[-1])
    result = []
    usedClothes = {}
    totalTime = 0
    counter = 0
    for lavado in orderedCombinations:
        if (lavado[0] not in usedClothes and lavado[1] not in usedClothes):
            counter += 1
            usedClothes[lavado[0]] = counter
            usedClothes[lavado[1]] = counter
            result.append((lavado[0], lavado[1]))
            totalTime += lavado[2]

    
    print("times: {}".format(times))
    print("combinations: {}".format(combinations))
    print("combinations: {}".format(orderedCombinations))
    print("result: {}".format(result))
    print("total time: {}".format(totalTime))
    print("Used Clothes: {}".format(usedClothes))
    file.close()
    resultFile = open("entrega_1.txt", "w")
    for lavado in usedClothes:
        resultFile.write("{} {}\n".format(lavado, usedClothes[lavado]))
    resultFile.close()

main()