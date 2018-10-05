import datetime

file = open("hardlopers.txt", "a+")

input = input("Vul een naam in: ")

def addName(input):
    vandaag = datetime.datetime.today()
    file.write(vandaag.strftime("%a %d %b %Y %Y-%m-%d %H:%M:%S") + " " + input + "\n")
    print("Done!")

addName(input)