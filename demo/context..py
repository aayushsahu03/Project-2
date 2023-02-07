from contextlib import contextmanager

class Open_File:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode

    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file

    def __exit__(self,exc_type,exc_val,traceback):
        self.file.close()

# with Open_File("./PROJECT1/demo/file1.txt",'w') as f:
#     f.write('yo yo')
# print(f.closed)

#*****************************************************************

@contextmanager
def open_file(file,mode):
    f=open(file,mode)
    yield f
    f.close()

with open_file("./PROJECT1/demo/file_temp.txt",'w') as f:
    f.write('yo yo')

print(f.closed)


import os

@contextmanager
def see_directory(path):
    try:
        cwd=os.getcwd()
        os.chdir(path)
        yield 
    except RuntimeError as e:
        print("sorry")

    finally:    
        os.chdir(cwd)    

with see_directory('./PROJECT'):
    print(os.listdir())



# os.chdir('./OS Module')
# print(os.listdir())
# os.chdir(cwd)

