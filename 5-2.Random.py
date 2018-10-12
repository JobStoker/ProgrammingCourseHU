import random

def monopolyworp():
    dobbelsteen1 = random.randint(1, 6)
    dobbelsteen2 = random.randint(1, 6)

    return dobbelsteen1, dobbelsteen2

worp = monopolyworp()

print(str(worp[0]) + " + " + str(worp[1]) + " = "  + str(worp[0] + worp[1]))

count = 1
while worp[0] == worp[1] and count < 4:
    worp = monopolyworp()
    print(str(worp[0]) + " + " + str(worp[1]) + " = " + str(worp[0] + worp[1]))
    count += 1
    if count == 3:
        print("Direct naar de gevangenis!")
