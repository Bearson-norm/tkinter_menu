import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

#resolusi layar dan  image recognition
width = 1600 #in pixels
height = 900 #in pixels
width_recognition = 672
height_recognition = 364

#Tentukan terlebih dahulu layar utamanya
window = tk.Tk()
window.geometry('500x500')
window.title('Tugas Pertama Pemrograman Lanjut')

#Tentukan fungsi untuk button
def memunculkan_foto():
    image = Image.open("pemlan2.jpeg")
    foto = ImageTk.PhotoImage(image)
    label_foto = tk.Label(window, image=foto)
    label_foto.image = foto
    label_foto.place(x=130, y=50)

    def nama():
        text = "Hilal Akbar Quddus Ramadhan\n11200970000035\nCiputat"
        label_nama = tk.Label(window, text=text)
        label_nama.place(x=180, y=400)
        print("Nama, NIM, dan alamat sudah terverifikasi")
        

    #button yang muncul saat eksekusi kode
    button_nama = tk.Button(window, text='Klik untuk memunculkan nama, NIM, dan alamat', command=nama)
    button_nama.place(x=110, y=300)

#Tentukan eksekusi kode, dan GUI nya
button_memunculkan_foto = tk.Button(window, text='Klik tombol ini untuk memunculkan foto', command=memunculkan_foto).pack()

window.mainloop()