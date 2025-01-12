print("Hello! What is your name?")
name = input("My name is:")
print('Where are you from?')
country = input('I am from:')
if country == 'Germany':
    print('Es freut mich sehr, dich kennenzulernen',name)
    print("Ciao!")
elif country == 'France':
    print('Enchanté de faire votre connaissance',name)
    print("Au revoir!")
elif country == 'Italy':
    print('È un piacere conoscerti',name)
    print("Arrivederci!")
else:
    print('Nice to meet you',name)
    print("Goodbye!")
