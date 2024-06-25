# dog3.py

class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles",4)
miles.description()
miles.speak("Woof Woof")


if __name__ == '__main__':
    buddy = Dog("Buddy",5)
    print(buddy.description())
    print(buddy.speak("Bow Bow"))
    print(miles.description())
