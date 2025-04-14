import os

os.system("mkdir txt")
os.system("mkdir jpg")
os.system("mkdir csv")
with open("./test.txt","r") as dir:
    for file in dir:
        print(file)
# move=os.system(f"mv {ext}")