# dog7.py

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"

class BorderCollie(Dog):
    def __init__(self, name, age, play_frisbee):
        super().__init__(name,age)
        self.play_frisbee = play_frisbee
    def description(self):
        if self.play_frisbee:
            return f"{self.name} is {self.age} years old and plays frisbee"
        else:
            return f"{self.name} is {self.age} years old"
    def speak(self, sound="Wow"):
       return super().speak(sound)
    
robert = BorderCollie("Robert",8,True)
robert.description()
robert.speak()