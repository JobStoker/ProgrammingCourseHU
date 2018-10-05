def convert(temperature):
    return temperature * 1.8 + 32

def table():
    print("F {:^15} C".format(' '))
    for i in range(-30, 41, 10):
        print('{:<10}{:>10}'.format(convert(i), i))


table()