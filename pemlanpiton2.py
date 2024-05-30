from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image

# Convert ICO to PNG
ico_image = Image.open('favicon.ico')
ico_image.save('favicon.png', format='PNG')

ico_image2 = Image.open('favicon (2).ico')
ico_image2.save('favicon(2).png', format='PNG')


jendela = tk.Tk()
jendela.title("Membuat Judul dan Button")
jendela.geometry('400x400')
jendela.iconbitmap('favicon.ico')
jendela['bg'] = '#856ff8'

def fungsinya():
    data = tk.Label(jendela, text="Lampu Menyala", background="blue")
    data.place(x=50, y=180)
    TOMBOL2 = ttk.Button(jendela, text="KLIK LAGI", command=buktinya)
    TOMBOL2.place(x=50, y=210)

def buktinya():
    data = tk.Label(jendela, text="Lampu Mati", bg="yellow", fg="blue")
    data.place(x=50, y=240)

def select(option):
    print(option)

label = tk.Label(jendela, text="Belajar Label dan Button", bg="yellow", fg="blue", padx=10, pady=10)
label.place(x=10, y=10)
label = tk.Label(jendela, text="Belajar Label", bg="yellow", fg="red", padx=10, pady=10)
label.place(x=20, y=70)
label = tk.Label(jendela, text="Belajar Button", bg="blue", fg="white", padx=10, pady=10)
label.place(x=250, y=70)

photo = tk.PhotoImage(file='favicon.png')
photo2 = tk.PhotoImage(file='favicon(2).png')

image_label = ttk.Label(jendela, text="Foto Lambang UIN", image=photo, compound='top')
image_label.pack()

Tombol = ttk.Button(jendela, text="START", command=fungsinya)
Tombol.place(x=50, y=150)

Exit_button = ttk.Button(jendela, text="EXIT", command=lambda: jendela.quit())
Exit_button.pack(ipadx=5, ipady=5, expand=True)

ttk.Button(jendela, text='Roda 1', command=lambda: select('Maju')).place(x=280, y=150)
ttk.Button(jendela, text='Roda 2', command=lambda: select('Mundur')).place(x=280, y=180)
ttk.Button(jendela, text='Roda 3', command=lambda: select('Berhenti')).place(x=280, y=210)
ttk.Button(jendela, text='TOMBOL HIDAYAH', image=photo2, compound='right').place(x=50, y=250)

jendela.mainloop()
