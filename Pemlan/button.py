from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
layar = tk.Tk()
layar.geometry('300x500')
layar_frame=tk.Frame(layar,bg='green',highlightbackground='white',highlightthickness=1)
layar_frame.pack(side=tk.TOP,fill=tk.X)
layar_frame.pack_propagate(False) # digunakan untuk mencocokan antara container dengan widget, jika false, maka widget tidak akan mencocokan ukurannya dengan container
layar_frame.configure(height=50) 
def isi():
    print(" sudah malam ngantuk ")

def open_profile_tab():
        # pass
        image = Image.open('me.ico')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(layar, text='My Photo',image=photo)
        label.place(x=200,y=100)
        label.image = photo

        def open_desc():
            desc = "Nama: Muhammad Fikry Rizal\nNIM: 11200970000053\nKelas: Instrumentasi"
            tk.Label(layar,text=desc,fg='black',font=("Arial", 12), justify='left').place(x=480,y=300)
        desc_button=tk.Button(layar,text='Klik',font=('Bold',20),bd=0,bg='green',fg='white',activebackground='green',activeforeground='white',command=open_desc)
        desc_button.place(x=300,y=380)
def toggle_menu():
    def colapse_toggle_menu():
        toggle_menu_fm.destroy() # ditujukan untuk menghapus suatu variabel
        toggle_button.config(text='=')
        toggle_button.config(command=toggle_menu)

    toggle_menu_fm=tk.Frame(layar,bg='green')
    toggle_menu_fm.place(x=0,y=50,height=500,width=200)

    home_button=tk.Button(toggle_menu_fm,text='Home',font=('Bold',20),bd=0,bg='green',fg='white',activebackground='green',activeforeground='white',command=isi)
    home_button.place(x=20,y=20)

    produc_button=tk.Button(toggle_menu_fm,text='Product',font=('Bold',20),bd=0,bg='green',fg='white',activebackground='green',activeforeground='white')
    produc_button.place(x=20,y=80)

    menu_button=tk.Button(toggle_menu_fm,text='Menu',font=('Bold',20),bd=0,bg='green',fg='white',activebackground='green',activeforeground='white')
    menu_button.place(x=20,y=140)
    
    profile_button=tk.Button(toggle_menu_fm,text='Profile',font=('Bold',20),bd=0,bg='green',fg='white',activebackground='green',activeforeground='white',command=open_profile_tab)
    profile_button.place(x=20,y=200)

    toggle_button.config(text='X')
    toggle_button.config(command=colapse_toggle_menu)
toggle_button=tk.Button(layar_frame,text='=',bg='green',fg='white',font=('Bold',20),bd=0,activebackground='green',activeforeground='white',command=toggle_menu)
toggle_button.pack(side=tk.LEFT)
title_lb=tk.Label(layar_frame,text='Tkinter menu',bg='green',fg='white',font=('Bold',20))
title_lb.pack(side=tk.LEFT)

layar.mainloop()