class Emp:
    def __init__(self,id,name,add):
        self.id=id
        self.name=name
        self.add=add
        print("Id : ",id)
        print("name : ",name)
        print("address : ",add)
class EmpDet(Emp):
    def __init__(self,id, name, add, email):
        super().__init__(id, name, add)
        self.email=email
        print("email : ",email)
details=EmpDet(34,"datta","Hyderabd", "dat@emap.com")



