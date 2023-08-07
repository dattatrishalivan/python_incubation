class parent:
    def show(self):
        print("parent class")
class child(parent):
    def show(self):
        super().show()
        print("chaild class")
c=child()
c.show()