from tkinter import *
from PIL import Image
import ntpath
import os
import math
import app as appy

def hspace(col,root):
    '''
    Adding horizontal space
    '''
    space = Label(root,text = "    ",bg = '#3ed8ea')
    space.grid(row=2,column=col)

def vspace(row,root):
    '''
    Adding Vertical Space
    '''
    space = Label(root,text = "  ",bg = '#3ed8ea')
    space.grid(row=row)

def leftClick(event,x):
    '''
    Left Click event to open image
    '''
    im = Image.open(x)
    im.show()

def run(fileList):
    '''
    Creates the window 
    '''
    root = Tk()
    root.title("Image Compression")
    root.geometry('1070x400')
    root.configure(background='#3ed8ea')
    root.resizable(True,False)
    appy.center(root)
    vspace(0,root)
    
    image_name = Label(root,text="Image Name",borderwidth=2, relief="solid",bg = '#3ed8ea',fg='#1c1c6c',height=2,width=25,font='Verdana 12')
    image_name.grid(row=2,column = 0)
    vspace(3,root) 
    hspace(1,root)
    oi = Label(root,text="Original Image Size",borderwidth=2, relief="solid",bg = '#3ed8ea',fg='#1c1c6c',height=2,width=25,font='Verdana 12')
    oi.grid(row=2,column=2)
    hspace(3,root)
    ci = Label(root,text="Compressed Image Size",borderwidth=2, relief="solid",bg = '#3ed8ea',fg='#1c1c6c',height=2,width=25,font='Verdana 12')
    ci.grid(row=2,column=4)
    hspace(5,root)
    cr = Label(root,text="Compression Ratio",borderwidth=2, relief="solid",bg = '#3ed8ea',fg='#1c1c6c',height=2,width=25,font='Verdana 12')
    cr.grid(row=2,column=6)

    rows = 4
    '''
    Adding the files in the list along with the size of original image and compressed image and also compression ratio
    '''
    for i in range(len(fileList)):
        name = ntpath.basename(fileList[i])
        compressed_file_name =  "Compressed_Images/"+name[:len(name)-4]+"_compressed"+name[len(name)-4:]
        create_table(root,name,fileList[i],compressed_file_name,rows)
        rows = rows+1
    mainloop()

def extract_ratio(str1,str2):
    '''
    Finds the compression ratio
    '''
    s1 = int(str1[:len(str1)-3])
    s2 = int(str2[:len(str2)-3])
    return "%.2f"%(s1/s2)
    
def create_table(root,name,file,file2,row):
    '''
    This is used for adding multiple images in the list. 
    On clicking the original image, it opens the original image
    On clicking the compressed image, it opens the compressed image
    '''
    image = Label(root,text=name,bg = '#3ed8ea',fg='#1c1c6c',font='Verdana 12')
    image.grid(row=row,column = 0)
    image1 = Label(root,text = meta_data(file),bg = '#3ed8ea',fg='#1c1c6c',font='Verdana 12')
    image1.grid(row=row,column = 2)
    image1.bind("<Button-1>",lambda event:leftClick(event,file))
    image1 = Label(root,text = meta_data(file2),bg = '#3ed8ea',fg='#1c1c6c',font='Verdana 12')
    image1.grid(row=row,column = 4)
    image1.bind("<Button-1>",lambda event:leftClick(event,file2))
    image1 = Label(root,text = extract_ratio(meta_data(file),meta_data(file2)),bg = '#3ed8ea',fg='#1c1c6c',font='Verdana 12')
    image1.grid(row=row,column = 6)

def meta_data(filen):
    '''
    Gives the file size of the selected file in Kb
    '''
    return str(math.ceil(int(os.path.getsize(filen))/1024)) + " Kb"
