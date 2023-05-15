class Person:
    species = "human"
    def __init__(self, name, age, gender):
        """
              Constructor for Person class.

              Args:
              name (str): Name of the person
              age (int): Age of the person
              gender (str): Gender of the person
              """
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        """
                Method to introduce the person.
                """
        print(f"Hi, my name is {self.name}, I'm {self.age} years old and I identify as {self.gender}.")

class Pet:
    """
     A class representing a pet.
     """

    species = "animal"

    def __init__(self, name, age, species, owner):
        """
             Constructor for Pet class.

             Args:
             name (str): Name of the pet
             age (int): Age of the pet
             species (str): Species of the pet
             owner (Person): Owner of the pet
             """
        self.name = name
        self.age = age
        self.species = species
        self.owner = owner

    def introduce(self):
        """
               Method to introduce the pet.
               """
        print(f"Hi, my name is {self.name}, I'm a {self.species} and my owner is {self.owner.name}.")

    @classmethod
    def from_birth_year(cls, name, birth_year, species, owner):
        """
              Class method to create a Pet instance based on birth year.

              Args:
              name (str): Name of the pet
              birth_year (int): Birth year of the pet
              species (str): Species of the pet
              owner (Person): Owner of the pet

              Returns:
              Pet instance with calculated age based on birth year.
              """
        import datetime
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        return cls(name, age, species, owner)

    @staticmethod
    def pet_years_to_human_years(pet_age):
        """
             Static method to convert pet years to human years.

             Args:
             pet_age (int): Age of the pet in pet years

             Returns:
             Age of the pet in human years.
             """
        return pet_age * 7



owner1 = Person("Vlad", 31, "male")
owner2 = Person("Sasha", 32, "female")

dog = Pet.from_birth_year("Ginger", 2022, "dog", owner1)
parrot = Pet("Shnufic", 4, "perrot", owner2)

owner1.introduce()
owner2.introduce()
dog.introduce()
parrot.introduce()

parrot.age += 1
print(f"{parrot.name} just had a birthday and is now {parrot.age} years old.")

dog_age_human_years = Pet.pet_years_to_human_years(dog.age)
print(f"{dog.name} is {dog_age_human_years} years old in human years.")
