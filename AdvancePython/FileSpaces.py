import os
f=open("C:\\Users\\Dattatri_Shalivan\\PycharmProjects\\pythonProject\\AdvancePython\\ConextTest1", "w")
f.write("dattatri")
f.write("\nshalivan godamgave auurad dfs")
f.close()
f=open("C:\\Users\\Dattatri_Shalivan\\PycharmProjects\\pythonProject\\AdvancePython\\ConextTest1", "r")
count=0
for i in f.read():
    if i==" ":
        count+=1
print(count)
f.close()
os.remove("C:\\Users\\Dattatri_Shalivan\\PycharmProjects\\pythonProject\\AdvancePython\\ConextTest1")
