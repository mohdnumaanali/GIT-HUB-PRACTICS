# # 4. Car Mileage Tracker
# class Car:
#     def __init__(self, brand, mileage=0):
#         self.brand = brand
#         self.mileage = mileage

#     def update_mileage(self, distance):
#         self.mileage += distance

# car1 = Car("Toyota", 12000)
# car1.update_mileage(500)
# print(car1.brand, "Mileage:", car1.mileag)


# 4. Car Mileage Tracker
class Car:
    def __init__(self, brand, mileage=0):
        self.brand = brand
        self.mileage = mileage

    def update_mileage(self, distance):
        self.mileage += distance

car1 = Car("Toyota", 12000)
car1.update_mileage(500)
print(car1.brand, "Mileage:", car1.mileage)