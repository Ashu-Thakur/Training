import os

# !CWD
# current_dir = os.getcwd()
# print(current_dir) # for getting the current working directory
# print(current_dir.split("/"))
# new_dir = "/".join(current_dir.split("/")[:-1])
# !Change working dir
# os.chdir("/home/developer/Desktop/Training_data_Enginnner")
# print(os.getcwd())

# List directory
print(os.listdir("/home/developer/Desktop/Training_data_Enginnner"))
# !sometime this \t can genrate errors so we can use raw string or can use \\ double slash
# ?make directories
# os.mkdir("codefile") # we can just make single directory
# ! if we want to make more directories and nested dir so we use 
# os.makedirs("codefile/demo/demo1", exist_ok= True)

# !remove directorirs
# os.rmdir("codefile",dir_fd=None)
# ?if the dir contain more dir or files then rmdir can't remove it ,it just remove one emty dir

# !Join the path
file = "text1.txt"
dir =os.getcwd()

newpath = os.path.join(dir, file) # can pass multi perameter to join in single path
print(newpath)

# path exist or not
print(os.path.exists(newpath)) # if exist return True otherwise false

# how to check that path is for file or dir
print(os.path.isfile(newpath)) # if file return True otherwise False
print(os.path.isdir(newpath)) # if dir return True otherwise False

# for gettting statics about file
print(os.stat("/home/developer/Desktop/Training_data_Enginnner/OS&File_handling/temp.txt").st_size)


# getting env varibale
print(os.environ.get('PATH')) #all environment varibales