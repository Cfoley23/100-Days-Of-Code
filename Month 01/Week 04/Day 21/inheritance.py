class Animal:

    def __int__(self):
        self.num_eyes = 2

    def breathe(self):
        print('Breathes the air')


class Cat(Animal):

    def __int__(self):
        super().__int__()

    def eat(self):
        print('Eats birds and rodents.')

wiley = Cat()

wiley.eat()
wiley.breathe()
print(wiley.num_eyes)
