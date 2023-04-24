from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #หน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม

GUI.geometry('500x400') #ขนาดโปรแกรท


L1 = Label(GUI,text='ร้านอาหาร',font=('Angsana New',25),fg='green')
L1.place(x=0,y=0)

def Button2():
    text = 'มีรายการอาหาร 5 รายการ'
    messagebox.showinfo('รายการอาหาร',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=100)
B2 = ttk.Button(FB1,text='ตรวจรายการอาหาร',command=Button2)
B2.pack(ipadx=20,ipady=20)


def Button3():
    text = 'มีโต๊ะว่างอยู่ 2 โต๊ะ'
    messagebox.showinfo('โต๊ะอาหารที่ว่าง',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=300,y=100)
B3 = ttk.Button(FB2,text='โต๊ะอาหาร',command=Button3)
B3.pack(ipadx=20,ipady=20)

def Button4():
    text = 'ตอนนี้มีเงินในร้าน 20000'
    messagebox.showinfo('เงินในบัญชี',text)

FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=300,y=350)
B4 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button4)
B4.pack(ipadx=20,ipady=20)






GUI.mainloop()
