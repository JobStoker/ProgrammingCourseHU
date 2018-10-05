file = open("Kaartnummers.txt", "r")

for i in file:
    print(i.replace(",", ":"))

file.close()