#name output program with a box

name = input('Enter name : ')
upperName = name.upper()
lowerName = name.lower()

print("|"+('-'*75)+'|')
print("|"+upperName.ljust(75)+"|")
print("|"+lowerName.center(75)+"|")
print("|"+upperName.rjust(75)+"|")
print("|"+('-'*75)+'|')