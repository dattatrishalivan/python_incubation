import os, filecmp
file1="C:\\Users\\Dattatri_Shalivan\\PycharmProjects\\pythonProject\\AdvancePython\\ConextTest"
file2="C:\\Users\\Dattatri_Shalivan\\PycharmProjects\\pythonProject\\AdvancePython\\ConextTest1"
f=open(file1, "r")
f1=open(file2, "w")
for i in f.read():
    f1.write(i)
f.close()
f1.close()
compare = filecmp.cmp(file1,file2)
if compare == True:
    print("The files are the same.")
else:
    print("The files are different.")
os.remove(file2)