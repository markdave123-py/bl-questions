from  abc import ABC

class Programmer:
    def __init__(self, name, laptop_model, lang='python'):
        self.laptop_model = laptop_model
        self.lang = lang
        self.name = name

    def coding(self):
        print(f'{self.name} is a codholic')


class Senior(Programmer):
    def __init__(self,  name, laptop_model, lang='python', headset_model='sony'):
        super().__init__(name, laptop_model, lang='python')
        self.headset_model = headset_model

    def greet(self):
        print(f'Hello Launchpad my name is {self.name} and i am senior DE')

Kabir = Senior('Kabir', 'Linux', 'C++', 'Sony')

Kabir.coding()

# a = Programmer()

Kabir.greet()



    


Adebola = Programmer("Adebola", 'Macbook')

Faruk = Programmer("Faruk", 'Linux', 'binary')

Adebola.coding()
Faruk.coding()

print(Adebola.laptop_model, Faruk.lang)


