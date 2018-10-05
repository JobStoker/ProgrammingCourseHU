leeftijd = int(input("Wat is je leeftijd: "))
paspoort = input("Heb je een Nederland paspoort?: ")

if leeftijd >= 18 and paspoort == "Ja":
    print("Gefeliciteerd je mag stemmen!")
elif leeftijd < 18 or paspoort == "Nee":
    print("Je mag niet stemmen..")