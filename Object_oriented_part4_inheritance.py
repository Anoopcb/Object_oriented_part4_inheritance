## inheritance

class Phone:

    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price =max(price, 0)

    def full_name(self):
        return f"{self.brand} {self.model_name}..."

    def make_a_call(self, number):
        return f"calling {number}"


class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_momery, rear_camera):
        #self.brand = brand
        #self.model_name = model_name
        #self.__price = max(price, 0)

       # Phone.__init__(self, brand, model_name, price)

        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_momery = internal_momery
        self.rear_camera = rear_camera

    def full_name(self):

        return f"{self.brand} {self.model_name} and price is {self._price}"

    #def make_a_call(self, number):
       # return f"calling {number}"

class FlagshipPhone(Smartphone):
    def __init__(self, brand, model_name, price, ram, internal_momery,rear_camera, front_camera):
        super().__init__( brand, model_name, price, ram, internal_momery,rear_camera)

        self.front_camera = front_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price} with front camera {self.front_camera}"


#phone = Phone("nokia", "1100", 10000)
smartphone = Smartphone("iphone", "xr", 900000, "8gb", "320gb", "20mp")
#print(phone.full_name())

superphone = FlagshipPhone("iphone", "11Plust", 900000, "8gb", "320gb", "20mp", "16mp")
print(smartphone.full_name())## this is multilevel inheritance

#print(smartphone.full_name()+ f"and price is {smartphone.price}")

print(superphone.full_name())

print(help(Smartphone))## this is for method resolution

#print(help(FlagshipPhone))


## multiple inheritance
