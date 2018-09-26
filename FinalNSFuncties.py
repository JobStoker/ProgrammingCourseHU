afstand  = input('Hoeveel KM moet je reizen: ')
weekend  = bool((input('Reis je in het weekend: '))
leeftijd = input('Wat is je leeftijd: ')




def standaardprijs(afstandKM):
    afstandberekenbaar = int(afstandKM)

    if afstandberekenbaar < 50 and afstandberekenbaar > 0:
        return afstandberekenbaar * 0.80
    elif afstandberekenbaar > 0:
        return afstandberekenbaar * 0.80 + (afstandberekenbaar - 50) * 0.60 + 15
    else:
        print('Je kunt geen negatieve afstand reizen')
        exit()


def ritprijs(leeftijd, weekendrit, afstandKM):
    standaard = standaardprijs(afstandKM)

    if weekendrit == False and leeftijd < 12 or weekendrit == False and leeftijd > 65:
        print(standaard * 0.70)
    elif weekendrit == True and leeftijd < 12 or weekendrit == True and leeftijd > 65:
        print(standaard * 0.65)
    elif weekendrit == True and leeftijd > 12 and leeftijd < 65:
        print(standaard * 0.60)
    else:
        print(standaard)

ritprijs(leeftijd, weekend, afstand)


