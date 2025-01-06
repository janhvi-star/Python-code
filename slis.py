class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

# Create an object of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)  # Output: Buddy
my_dog.bark()  # Output: Woof!