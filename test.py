from tkinter import *
from tkinter.filedialog import askopenfilenames
from fpdf import FPDF

import img2pdf
from tkinter import ttk
from PIL import ImageTk, Image
root = Tk()
root.title("IMAGE TO PDF CONVERTER")
root.geometry("720x1080")
root.iconbitmap("D:logox.ico")
root.configure(background='powder blue')


def select_file():
    global file_names
    file_names = askopenfilenames(initialdir = "/",
                                  title = "Select File")
# IMAGE TO PDF
def image_to_pdf():
 for index, file_name in enumerate(file_names):
  with open(f"file {index}.pdf", "wb") as f:f.write(img2pdf.convert(file_name))

#Convert Image to PDF
def images_to_pdf():
  with open(f"file.pdf", "wb") as f:f.write(img2pdf.convert(file_names))

def button_press(var):
    if one:
        x = 1
        display.configure(bgco=x)
    if two:
        x = 2
        display.configure(bgco2=x)

#convert text into pdf


# save FPDF() class into
# a variable pd
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size=15)

# open the text file in read mode

f = open("pytx.txt", "r")
for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align='C')

# insert the texts in pdf
def text_to_pdf():
    pdf.output("ttp.pdf")


# save the pdf with name .pdf
pdf.output("ttp.pdf")




frame = Frame(root)
frame.pack()
frame.configure(background="powder blue")
#frame 2 for  text to pdf
frame2 = Frame(root)
frame2.pack(side="left")
frame2.configure(background="powder blue")


bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

pic = ImageTk.PhotoImage(file="e:\hello world/logoz.png")
logo = Label(frame,image=pic,height=50,width=80)
logo.pack(side="left")


my_label = Label(frame,text="IMAGE TO PDF CONVERTER",font=("berlin sans fb demi",26) ,bd=4,bg="orange",relief="raised")
my_label.pack(pady=20)
uplodBut = Button(root,text="UPLOAD IMAGES", command = select_file,font=("berlin sans fb demi",14),bg="orange",padx=20,pady=10)
uplodBut.pack(side="left",padx=10,pady=10)


clicBut = Button(root,text="CONVERT SINGLE IMG",command = image_to_pdf,font=("berlin sans fb demi",14),bg="orange",padx=20,pady=10)
clicBut.pack(side="left",padx=10,pady=10)
clicBut = Button(root,text="CONVERT MULTIPLE IMG",command = images_to_pdf,font=("berlin sans fb demi",14),bg="orange",padx=20,pady=10)
clicBut.pack(side="left",padx=10,pady=10)
#frame2buttons
clicBut = Button(frame2,text="TEXT FILE",command =select_file,font=("berlin sans fb demi",14),bg="orange",padx=20,pady=10)
clicBut.pack(side="bottom",padx=0,pady=150)
clicBut = Button(frame2,text="CONVERT TEXT TO PDF",command = text_to_pdf,font=("berlin sans fb demi",14),bg="orange",padx=20,pady=10)
clicBut.pack(side="bottom",padx=10,pady=150)


pic2 = PhotoImage(file="e:\hello world\pyimage/handwriting.png")

bgco=Label(root,image=pic2, height=700,width=600)
bgco.pack(side="left")

root.mainloop()