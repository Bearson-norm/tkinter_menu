import tkinter as tk
from tkinter import Menu, filedialog
from PIL import Image, ImageTk
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

layar = tk.Tk()
layar.geometry('500x500')
layar_frame=tk.Frame(layar,bg='green',highlightbackground='white',highlightthickness=1)
layar_frame.pack(side=tk.TOP,fill=tk.X)
layar_frame.pack_propagate(False) # digunakan untuk mencocokan antara container dengan widget, jika false, maka widget tidak akan mencocokan ukurannya dengan container
layar_frame.configure(height=50) 

def plot_graph():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    data = {'X Data': [0, 2, 4, 6, 8, 10, 13, 14, 16, 18, 20],
            'Y1 Data': [5, 6, 4, 10, 15, 14, 20, 6, 4, 8, 9],
            'Y2 Data': [15, 30, 20, 45, 10, 10, 12, 13, 18, 25, 12],
            'Y3 Data': [100, 125, 122, 128, 79, 84, 99, 56, 67, 83, 91]}

    df = pd.DataFrame(data)

    ax1.plot(df['X Data'], df['Y1 Data'], label='Y1 Data')
    ax1.plot(df['X Data'], df['Y2 Data'], label='Y2 Data')
    ax1.plot(df['X Data'], df['Y3 Data'], label='Y3 Data')

    ax1.set_xlabel('X Data')
    ax1.set_ylabel('Values')
    ax1.set_title('Line Plot from Data')
    ax1.legend()

    ax2.bar(df['X Data'], df['Y1 Data'], label='Y1 Data')
    ax2.bar(df['X Data'], df['Y2 Data'], label='Y2 Data')
    ax2.bar(df['X Data'], df['Y3 Data'], label='Y3 Data')

    ax2.set_xlabel('X Data')
    ax2.set_ylabel('Values')
    ax2.set_title('Bar Plot from Data')
    ax2.legend()

    canvas = FigureCanvasTkAgg(fig, master=layar)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def menu_isi():
    # Label untuk judul
    title_label = tk.Label(layar, text="Biodata Mahasiswa", font=("Helvetica", 16), bg="light blue")
    title_label.pack(pady=10)
    # Label untuk gambar mahasiswa
    image_label = tk.Label(layar, bg="light blue")
    image_label.pack()
    def open_image():
        filename = filedialog.askopenfilename(title="Pilih gambar mahasiswa")
        if filename:
                img = Image.open(filename)
                img = img.resize((200, 200), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)
                image_label.config(image=img)
                image_label.image = img
    # Tombol untuk mengunggah gambar
    upload_button = tk.Button(layar, text="Unggah Foto", command=open_image)
    upload_button.pack(pady=10)
    # Entry untuk Nama dan NIM
    nama_label = tk.Label(layar, text="Nama Mahasiswa: Ary Prasetyo Cahyono", bg="light blue")
    nama_label.pack()
    nim_label = tk.Label(layar, text="NIM: 11210970000038", bg="light blue")
    nim_label.pack()
    nim_teks1 = tk.Label(layar, text="Fisika instrumentasi adalah salah satu kajian terapan dari ilmu fisika yang berfokus pada pengukuran dan pengaturan besaran fisik secara langsung atau tidak langsung.", bg="light blue")
    nim_teks1.pack()
    # Tombol untuk menampilkan grafik
    graph_button = tk.Button(layar, text="Tampilkan Grafik", command=plot_graph)
    graph_button.pack(pady=10)
    # Tombol untuk keluar dari program
    exit_button = tk.Button(layar, text="Keluar", command=exit_program)
    exit_button.pack(pady=10)

def exit_program():
    layar.destroy()

def toggle_menu():
    def colapse_toggle_menu():
        toggle_menu_fm.destroy() # ditujukan untuk menghapus suatu variabel
        toggle_button.config(text='=')
        toggle_button.config(command=toggle_menu)

    toggle_menu_fm=tk.Frame(layar,bg='green')
    toggle_menu_fm.place(x=0,y=50,height=500,width=200)

    # Menu
    menu_button=tk.Button(toggle_menu_fm,text='Menu',font=('Bold',20),bd=0,bg='green',fg='white',activebackground='green',activeforeground='white', command=menu_isi)
    menu_button.place(x=20,y=20)

    # Collapse
    toggle_button.config(text='X')
    toggle_button.config(command=colapse_toggle_menu)

toggle_button=tk.Button(layar_frame,text='=',bg='brown',fg='white',font=('Bold',20),bd=0,activebackground='green',activeforeground='white',command=toggle_menu)
toggle_button.pack(side=tk.LEFT)
title_lb=tk.Label(layar_frame,text='PEMLAN UTS',bg='yellow',fg='white',font=('Bold',20))
title_lb.pack(side=tk.LEFT)

layar.mainloop()