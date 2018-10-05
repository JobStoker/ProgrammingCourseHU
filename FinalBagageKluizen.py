option = input("1: Ik wil weten hoeveel kluizen nog vrij zijn: \n2: Ik wil een nieuwe kluis: \n3: Ik wil even iets uit mijn kluis halen: \n")
option = int(option)

def toon_aantal_kluizen_vrij():

    file = open("kluizen.txt", "r")
    count = file.readlines()

    file.close()

    print(12 - len(count))

def nieuwe_kluis():

    file = open("kluizen.txt", "r+")
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    #Kijken welke list nummers er in tekstbestabd staan
    for i in file:
        #Split kluisnummer na de ;
        kluisnummer = i.split(";")[0]

        if int(kluisnummer) in list:
            list.remove(int(kluisnummer))

    if len(list) > 0:
        code = input("Voer een code in: ")
        file.write(str(list[0]) + ";" + code + "\n")
        print("Uw kluisnummer = " + str(list[0]))
    else:
        print("Er zijn geen kluizen meer beschikbaar!")

    file.close()

def kluis_openen():

    file = open("kluizen.txt", "r")

    kluis = input("Voer je kluisnummer in: ")
    code = input("Voer je kluiscode in: ")
    kluiscombinatie = (kluis + ";" + code)
    kluizen = []

    for i in file:

        i = i.replace("\n", "")
        kluizen.append(i)

    if kluiscombinatie in kluizen:
        print("Je kluis is open!")
    elif kluiscombinatie not in kluizen:
        print("Je hebt geen geldige kluis combinatie ingevoerd")

    file.close()

if option == 1:
    toon_aantal_kluizen_vrij()
elif option == 2:
    nieuwe_kluis()
elif option == 3:
    kluis_openen()
else:
    print("Je hebt een foute optie ingevoerd")