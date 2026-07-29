# # here we are going to start new question and it is 3 
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# rect = Rectangle(10, 5)
# print("Area:", rect.area(), "Perimeter:", rect.perimeter())

class Rectriangle :
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length  * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

result = Rectriangle(20 , 10)
print("area", result.area() , "parimeter" , result.perimeter() )            #area 200 parimeter 60