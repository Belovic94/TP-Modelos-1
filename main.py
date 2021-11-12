class LaundrySet:
    def __init__(self, time, clothes, incompatibilities):
        self.time = time
        self.clothes = clothes
        self.incompatibilities = incompatibilities
    
    def __repr__(self):
        return "(time: {}, clothes: {}, incompatibilities: {})".format(self.time, self.clothes, self.incompatibilities)

    def __str__(self):
        return "(time: {}, clothes: {}, incompatibilities: {})".format(self.time, self.clothes, self.incompatibilities)   
    
    def combine(self, other):
        if (self.time < other.time):
            self.time = other.time
        self.clothes = self.clothes + other.clothes
        self.incompatibilities = list(set(self.incompatibilities) | set(other.incompatibilities))

    def isCompatible(self, other):
        return list(set(self.incompatibilities) & set(other.clothes)) + list(set(self.clothes) & set(other.incompatibilities)) == []

def write_results(laundry_sets):
    total_time = 0
    resultFile = open("result.txt", "w")
    laundry_counter = 1
    for x in laundry_sets:
        for j in laundry_sets[x]:
            total_time += j.time
            for k in j.clothes:
                resultFile.write("{} {}\n".format(k, laundry_counter))
            laundry_counter += 1
    print("total time: {}".format(total_time))
    resultFile.close()

def main():
    times = {}
    incompatibilities = {}
    clothes = 0
    max_time = 0
    file = open('enunciado2.txt', 'r')
    for line in file:
        row = line.split()
        if row[0] == 'p':
            clothes = int(row[2])
        elif row[0] == 'e':
            if (row[1] in incompatibilities):
                incompatibilities[row[1]].append(row[2])
            else:
                incompatibilities[row[1]] = [row[2]]
        elif row[0] == 'n':
            time = int(row[2])
            if (max_time == 0 or time > max_time):
                max_time = time
            times[row[1]] = time
    
    laundry_sets = []
    #Genero los conjuntos
    for i in range(1, clothes + 1):
        index = str(i)
        laundry_sets.append(LaundrySet(times[index], [index], incompatibilities.get(index, [])))

    print("{}\n".format(laundry_sets))
    dicc_laundry_set = {}
    step = 2
    visits_sets = 0
    for i in range(1, max_time + 1, step):
        first_index = i
        last_index = i + step - 1 if (i + step - 1) <= max_time else max_time
        time_laundry_set = [x for x in laundry_sets if x.time in range(first_index, last_index + 1)]
        bucket = []
        print("Bucket: {}\n".format((first_index, last_index)))
        for laundry_set in time_laundry_set:
            visits_sets += 1
            if (bucket == []):
                bucket.append(laundry_set)
            else:
                added = False
                for laundry_set_for in bucket:
                    if (laundry_set_for.isCompatible(laundry_set)):
                        laundry_set_for.combine(laundry_set)
                        added = True
                        break
                if (not added):
                    bucket.append(laundry_set)
        dicc_laundry_set[(first_index, last_index)] = bucket
    
    print(visits_sets)
    write_results(dicc_laundry_set)
    file.close()
   
main()