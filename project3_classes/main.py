class Car:
    def __init__(self, brand: str, model: str, color: str, 
                 weight: int, year: int):
        self.brand = brand
        self.model = model
        self.weight = weight
        self.is_running = False  # nie jest odpalone
        self.current_speed = 0
        self.odometer = 0
        self.color = color
    
    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_weight(self):
        return self.weight

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def set_brand(self, brand):
        self.brand = brand 

    def set_model(self, model):
        self.model = model

    def set_weight(self, weight):
        self.weight = weight
    
    def set_year(self, year):
        self.year = year
    
    def check_running(self):
        if self.is_running == False:
            print("auto nie jest odpalone")
        else:
            print("auto jest odpalone")
    
    def run_car(self):
        if self.is_running == False:
            self.is_running = True
        else:
            print("Auto juz jest odpalone")

    def stop_car(self):
        if self.is_running == False:
            print("Auto jest juz zgaszone")
        elif self.current_speed != 0:
            print("Auto jest w ruchu, nie mozna go zgaisc, zahamuj najpierw")
        else:
            self.is_running = False

    def break_to_zero(self):
        self.current_speed = 0

    def get_current_speed(self):
        return self.current_speed 

    def set_current_speed(self, current_speed):
        if self.is_running == True:
            self.current_speed = current_speed
        else:
            print("Auto jest zgaszone, nie da sie ustawic predkosci")

    def get_odometer(self):
        return self.odometer 

    def set_odometer(self, odometer):
        self.odometer = odometer

    def accelerate(self, increment):
        if self.is_running == True:
            self.current_speed += increment
        else:
            print("Auto zgaszone, nie da sie przyspieszyc")


if __name__ == '__main__':
    car1 = Car(brand="Audi", model="A4", weight=1800, year=2023, color="red")

    print(car1.get_color())
    car1.set_color("blue")
    print(car1.get_color())

    print(car1.get_brand())
    car1.set_brand("BMW")
    print(car1.get_brand())

    car1.check_running() 
    car1.run_car()
    car1.check_running() 
    car1.stop_car()
    car1.check_running() 
    
    car1.run_car()
    car1.accelerate(20)
    print(car1.get_current_speed())
    car1.stop_car()
    car1.break_to_zero()
    car1.stop_car()
    car1.check_running()
