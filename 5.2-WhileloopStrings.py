word = input("Geef een string van 4 letters: ")

while len(word) != 4:
    print(word + " heeft " + str(len(word)) + " letters")
    word = input("Geef een string van 4 letters: ")

print("Inlezen van correcte string: " + word + " is geslaagd")