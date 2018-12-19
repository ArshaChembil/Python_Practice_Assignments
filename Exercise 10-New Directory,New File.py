'''Exercise 10 -write a program to create a new directory, create a new file,
       list the directory using system commands( use os.system or subprocess.check_output module) '''

# import the os module
import os

# detect the current working directory and print it
path = os.getcwd()
print ("The current working directory is %s" % path)

'''Creating a New Directory'''
# define the name of the directory to be created
path = "\Sample_Test_xyz"
try:
    os.mkdir(path) #For creating multiple sub-directories use makedirs()
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)
print(os.listdir(os.getcwd()))
