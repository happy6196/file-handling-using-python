import os
import openpyxl as ox
s=3
path = os.getcwd()+'\\upload_your_images_here'
for folder_path, folders, files in os.walk(path):
    print(files)
wb=ox.load_workbook("images.xlsx")
ws=wb.active
for i in files:
    s+=1
    ws['B'+str(s)].value=str(i)

wb.save("all_your_images_names.xlsx")
os.startfile("all_your_images_names.xlsx")
