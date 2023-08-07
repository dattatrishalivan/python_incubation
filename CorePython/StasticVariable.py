class static:
    name="dattatri"
    def __init__(self,age,add):
        self.age=age
        self.add=add
st=static(20,'bidar')
st1=static(201,'bidar1')
print(st.name)
print(st.age)
print(st.add)
st.name="amit" # chnages only st.name value
#static.name='amit' changes both st.name and st1.name value
print(st.name)
print(st1.name)
