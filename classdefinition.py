class Car:
    def __init__(self, model, manufacturer, year):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        
    def descriptive_message(self):
        print(f"my {self.model} was created by {self.manufacturer} in {self.year}")

mycar = Car("Dena+", "irankhodro", 1400 )
mycar.descriptive_message()