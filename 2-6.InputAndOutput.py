uurloon = input('Uurloon: ')
werkuren = input('Aantal werkuren: ')

int(uurloon)
int(werkuren)

salaris = int(werkuren)*int(uurloon)

print('Je verdient: ' + str(uurloon) + ' per uur')
print('Je hebt: ' + str(werkuren) + ' uren gewerkt')
print(str(werkuren) + ' uur levert ' + str(salaris) + ' Euro op')