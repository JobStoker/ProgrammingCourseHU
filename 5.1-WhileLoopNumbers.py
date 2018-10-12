number = int(input("Geef een getal: "))

count = 0
sum = number

while number != 0:
    number = int(input("Geef een getal: "))
    count += 1
    sum += number

print("Er zijn " + str(count) + " getallen ingevoerd, de som is: " + str(sum))