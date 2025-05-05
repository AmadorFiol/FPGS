import os
def mover(ext,file):
    os.system(f"move {file} {ext}/{file}")
    log.write(f"El archivo {file} se ha movido a {ext}\n")

log=open("log.txt","a")
dir=os.listdir("./")
print(dir)
for file in dir:
    try:
        ext=file.split(".")[1]
        if file=="app.py" or file=="log.txt":
            pass
        elif ext not in dir:
            os.system(f"mkdir {ext}")
            dir.append(ext)
            log.write(f"Se ha creado la carpeta {ext}\n")
            mover(ext,file)
        else:
            mover(ext,file)
    except IndexError:
        pass
log.close()
dir=os.listdir("./")
print(dir)