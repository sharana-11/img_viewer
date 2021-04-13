from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('CUTIE PIE')
root.iconbitmap('C:\gui\project2\im1.ico')
my_img1=ImageTk.PhotoImage(Image.open('C:\gui\project2/cutie7.png'))
my_img2=ImageTk.PhotoImage(Image.open('C:\gui\project2/cutie8.png'))
my_img3=ImageTk.PhotoImage(Image.open('C:\gui\project2/cutie9.png'))
my_img4=ImageTk.PhotoImage(Image.open('C:\gui\project2/cutie11.png'))
my_img5=ImageTk.PhotoImage(Image.open('C:\gui\project2/cutie12.png'))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]
my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)
status=Label(root,text='Image of '+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
def next1(img_num):
    global my_label
    global button_next1
    global button_back
    my_label.grid_forget()
    my_label=Label(image=image_list[img_num-1])
    button_next1=Button(root,text='>>',command=lambda:next1(img_num+1))
    button_back=Button(root,text='<<',command=lambda:back(img_num-1))

    if img_num==5:
        button_next1=Button(root,text='>>',state=DISABLED)
    
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=5,column=0)
    button_next1.grid(row=5,column=2)
    #update status bar
    status=Label(root,text='Image'+str(img_num)+' of '+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    
def back(img_num):
    global my_label
    global button_next1
    global button_back
    my_label.grid_forget()
    my_label=Label(image=image_list[img_num-1])
    button_next1=Button(root,text='>>',command=lambda:next1(img_num+1))
    button_back=Button(root,text='<<',command=lambda:back(img_num-1))

    if img_num==1:
        button_back=Button(root,text='<<',state=DISABLED)
    
    
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_next1.grid(row=1,column=2)
    #update status bar
    status=Label(root,text='Image'+str(img_num)+' of '+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

button_back=Button(root,text='<<',command=back,state=DISABLED)
button_exit=Button(root,text='EXIT',command=root.quit)
button_next1=Button(root,text='>>',command=lambda:next1(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_next1.grid(row=1,column=2,pady=10)


status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()
