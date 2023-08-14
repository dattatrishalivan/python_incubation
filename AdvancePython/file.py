import os
f=open("C:\\Users\\Dattatri_Shalivan\\PycharmProjects\\pythonProject\\AdvancePython\\ConextTest1", "w")
f.write("dattatri")
f.write("\nshalivan godamgave")
f.close()
f=open("C:\\Users\\Dattatri_Shalivan\\PycharmProjects\\pythonProject\\AdvancePython\\ConextTest1", "r")
print(f.tell())
print(f.read())
print(f.tell())

f.close()
os.remove("C:\\Users\\Dattatri_Shalivan\\PycharmProjects\\pythonProject\\AdvancePython\\ConextTest1")
