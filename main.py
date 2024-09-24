#Open and store the content within greetings.txt to a variable before printing it.
f = open('greeting.txt', 'r')
greetings = f.read()
print(greetings)
f.close()

userInput = input('User choice: ')