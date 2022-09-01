import shutil
import os
from_dir="C:/Users/manya/Downloads/project 102"
to_dir="C:/Users/manya/OneDrive/Desktop/Document_files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,ext=os.path.splitext(file_name)
    print(name)
    print(ext)
    if ext=="":
        continue
    if ext in [".gif",".jfif",".png",".jpg",".jpeg"]:
        path1=from_dir+"/"+file_name
        path2=from_dir+"/"+"Document_Files"
        path3=path2
        if os.path.exists(path2):
            shutil.move(path1,path2)
        else:
            os.mkdir(path2)
            shutil.move(path1,path2)