import random
# TODO: Refer to the objective and sample output and figure out your own code!
# Time to graduate :p
name = input("What is your name? ")
animal = ["Shadow", "Phoenix", "Viper", "Falcon", "Wolf"]
adjective = ["Mighty", "Swift", "Cunning", "Brave", "Silent"]
print(f'{name},your codename is {random.choice(adjective)}{random.choice(animal)} and your lucky number is {random.randint(1, 99)}')

