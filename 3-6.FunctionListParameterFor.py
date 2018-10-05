grondgetallen = [ 4, 5, 3, -81 ]

def kwadraten_som(grondgetallen):
    total = 0
    for i in grondgetallen:
        if i > 0:
            total = total + i * i

    print(total)

kwadraten_som(grondgetallen)
