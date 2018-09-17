inputlength = input('Je lengte: ')

def lang_genoeg(length):
    if length >= 120:
        return 'Je bent lang genoeg voor de attractie!'
    else:
        return 'Sorry, je bent te klein!'


print(lang_genoeg(int(inputlength)))
