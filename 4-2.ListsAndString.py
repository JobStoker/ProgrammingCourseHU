#["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"]

list = eval(input("Geef lijst met minimaal 10 strings: "))
newlist = []
for i in list:
    if len(i) <= 4:
        newlist.append(i)


print(newlist)