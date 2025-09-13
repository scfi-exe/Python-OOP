# 1. Define a Class named Pet
# 2. Define a method for initialization: def __init__(self,name,species):
# 3. Inside the __init__ method, initialize two attributes:
#    self.name: assign the value of the name parameter
#    self.species: assign the value of the species parameter.


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species


# Do not modify below this line
my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")
