FirstName = str(input("please enter your first name: "))
LastName = str(input("please enter your last name: "))
CityBorn = str(input("please enter the city where you were born: "))
MotherMaidenName = str(input("please enter your mothers maiden name: "))
SpaceVar = str(" ")

StarWarsVar = (FirstName[0:3]+LastName[0:2]+SpaceVar+MotherMaidenName[0:2]+CityBorn[0:3])
print(StarWarsVar)