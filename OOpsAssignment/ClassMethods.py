"""Add a method set_marks(marks_ list), that takes a list of marks in 5 subjects and stores in a
new attribute marks. Also add a method print_details(), to student class to print average of marks and all details of student.
(Hint : average will be calculated as (total marks)/5 ) Test your class against the following code:
if __name__ == â€˜__main__â€™:
s = Student(â€˜abcâ€™, 20)
s.set_marks([80,60,90,70,99])
s.print_details()"""
class StudentAvg:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_marks(self, marks):
        totmar = 0
        for i in marks:
            totmar += i
        self.avg2 = (totmar) / 5

    def print_details(self):
        print("name : ", self.name)
        print("Age : ",self.age)
        print("Average : ",self.avg2)


s = StudentAvg('datta', 33)
s.set_marks([60, 70, 80, 65, 75])
s.print_details()