sentence = input("Voer een willekeurige zin in: ")

def gemiddelde(sentence):
    sentence = sentence.split()
    total = 0
    for i in sentence:
        total = total + len(i)

    return total / len(sentence)

print(gemiddelde(sentence))