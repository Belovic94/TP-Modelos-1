def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def main():
    combinations = []
    compatibilities = {}
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
        compatibilities[firstIndex] = []
        for j in range(1, clothes + 1):
            secondIndex = str(j)
            if ( firstIndex != secondIndex and secondIndex not in incompabilities[firstIndex]):
                compatibilities[firstIndex].append(secondIndex)
                time = times[firstIndex] if times[firstIndex] > times[secondIndex] else times[secondIndex]
                if (([secondIndex, firstIndex], time) not in combinations):
                    combinations.append(([firstIndex, secondIndex], time))
    
    triCombinations = []
    for i in range(1, clothes + 1):
        index = str(i)
        for combination in combinations:
            combinationList = combination[0]
            intersections = intersection(compatibilities[combinationList[0]], compatibilities[combinationList[1]])
            if (index not in combination[0] and index in intersections):
                time = times[index] if times[index] > combination[1] else combination[1]
                if (([secondIndex, firstIndex, index], time) not in combinations):
                    triCombinations.append((combinationList + [index] , time))
    
    newCombinations = triCombinations + combinations
    newCombinations = list(map(lambda x: (x[0], x[1], x[1]/len(x[0])), newCombinations))

    orderedCombinations = sorted(newCombinations, key=lambda x: x[-1])
    result = []
    usedClothes = {}
    totalTime = 0
    counter = 0
    for laundry in orderedCombinations:
        check = any(item in laundry[0] for item in usedClothes)
        if (check is False):
            counter += 1
            for cloth in laundry[0]:
                usedClothes[cloth] = counter
            result.append(laundry[0])
            totalTime += laundry[1]
    for x in times:
        if x not in usedClothes:
            counter += 1
            usedClothes[x] = counter
            totalTime += times[x]
    print("total time: {}".format(totalTime))
    file.close()
    resultFile = open("result.txt", "w")
    for lavado in usedClothes:
        resultFile.write("{} {}\n".format(lavado, usedClothes[lavado]))
    resultFile.close()

main()