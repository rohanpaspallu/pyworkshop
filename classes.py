class Car:
    runs: True

    def start(self):
        if self.runs:
            print("Car started")
        else:
            print("Car won't start")

my_car = Car()
my_car.runs = False
my_car.start()