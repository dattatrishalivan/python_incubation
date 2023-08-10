# with open("C:\\Users\\Dattatri_Shalivan\\Documents\\test1.txt") as file:
#     data = file.read()
#     print(data)
# file_descriptors = []
# for Y in range(10000):
#     file_descriptors.append( open ('C:\\Users\\Dattatri_Shalivan\\Documents\\test1.txt', 'w'))

class file_manager:
    def __init__(self, file_name, mode):
        self.filename = file_name
        self.mode = mode
        self.file = None
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
# At last, load the file
with file_manager('C:\\Users\\Dattatri_Shalivan\\PycharmProjects\\pythonProject\\AdvancePython\\ConextTest', 'w') as file:
    file.write('JavaTpoint')
print (file.closed)