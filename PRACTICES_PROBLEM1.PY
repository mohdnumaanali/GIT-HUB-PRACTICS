# STUDENT MARKS CALCULATER 

class Student :
    def __init__(self,names,roll_no , marks):
        self.names = names
        self.roll_no = roll_no
        self.marks = marks

    def calc(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("numaan",1,[90,90,90,90,90,90])
print(s1.names, s1.roll_no , "average" , s1.calc())