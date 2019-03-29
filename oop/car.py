
from vehicle import Vehicle

class Car(Vehicle):
    # top_speed = 100
    # warnings = []
    def __init__(self,starting_top_speed=100):
        self.top_speed = starting_top_speed
        self.__warnings = [] #private attribute ___

    def __repr__(self):
        print('Printing...')
        return 'Top speed: {}, Warnings: {}'.format(self.top_speed,len(self.__warnings))
    
    def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warnings.append(warning_text)

    def get_warnings(self):
        return self.__warnings

    def drive(self):
        print('I am driving but not faster than {}'.format(self.top_speed))
    
    def brag(self):
        print('Look how cool my car is!')

car1 = Car()
car1.drive()

#Car.top_speed = 200
car1.add_warning('New Warning')
#print(car1.__dict__)
print(car1)

car2 = Car()
car2.drive()
#print(car2.__warnings)