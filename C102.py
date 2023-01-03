import os
import shutil

from_Dir=r"C:\Users\\sai\\Desktop\\prathamesh whitehat .jr\\Python\\c102\\C102_assets-main"
to_Dir=r"C:\Users\\sai\\Desktop\\prathamesh whitehat .jr\\Python\\c102"

list_of_file=os.listdir(from_Dir)
print(list_of_file)
for file_Name in list_of_file:
   name,extention= os.path.splitext(file_Name) 

   if extention =='':
     continue   
   if extention in [".gif",".png",".jpg",".jpeg"".jfif"]:
         
    path1 = from_Dir + "/" + file_Name
    path2 = to_Dir + '/' + "Images_Files"       
    path3 = to_Dir + '/' + "Images_Files" + file_Name
    print("path1",path1)
    print("path3",path3)

    if os.path.exists(path2):
     print("Moveing" + file_Name + ".....")
     shutil.move(path1,path3)
    else:
     os.makedirs(path2)   
     print("Moveing" + file_Name + ".....")
     shutil.move(path1,path3)