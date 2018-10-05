file = open("Kaartnummers.txt", "r")

def countLines():
    file = open("Kaartnummers.txt", "r")
    total = 0
    for i in enumerate(file):
        total = i[0]
    return total + 1

def highestNumber():
    list = []
    for i in enumerate(file):
        list.append(i[1].split(',')[0])
    return "Het grootste kaartnummer is : " + str(max(list)) + " en dat staat op regel " + str(list.index(max(list)) + 1)

print("Deze file telt " + str(countLines()) + " regels")
print(highestNumber())