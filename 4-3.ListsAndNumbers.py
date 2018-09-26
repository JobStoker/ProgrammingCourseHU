invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

list = invoer.split("-")
list = [int(i) for i in list]

print("Gesorteerde list van ints: " + str(sorted(list)))
print("Grootste getal: " + str(max(list)) + " Kleinste getal: " + str(min(list)))
print("Aantal getallen: " + str(len(list)) + " Som van de getallen: " + str(sum(list)))
print("Gemiddelde: " + str(sum(list) / len(list)))