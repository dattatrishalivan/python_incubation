class StudDet:
    def details(self, name, age, add):
        print("name : ",name)
        print("age : ",age)
        print("address : ",add)

class StudContDet:
    def contact_details(self, phone, email):
        print("phone num : ",phone)
        print("email : ",email)

class marks(StudDet,StudContDet):
    def marks(self,m1,m2,m3):
        print("marks1 : ",m1)
        print("marks2 : ",m2)
        print("marks3 : ",m3)
M=marks()
M.details("datta",34,"Hyderabad")
M.contact_details(9945,"abcd@epam.com")
M.marks(78,98,80)

