naam = 'Job'
beginstation = 'Amsterdam'
eindstation = 'Utrecht'

string = naam + beginstation + eindstation


def code(string):
    newstring = ''

    for i in string:
        newstring += chr(ord(i) + 3)

    return newstring

print(code(string))