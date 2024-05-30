from tkinter import *
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def isi():
    print(" sudah malam ngantuk ")

def toggle_menu():

    def colapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_button.config(text='=')
        toggle_button.config(command=toggle_menu)

    toggle_menu_fm = tk.Frame(layar, bg='green')
    toggle_menu_fm.place(x=0, y=50, height=500, width=200)
    home_button = tk.Button(toggle_menu_fm, text='Home', font=('Bold', 20), bd=0, bg='green', fg='white',
                            activebackground='green', activeforeground='white', command=isi)
    home_button.place(x=20, y=20)
    produc_button = tk.Button(toggle_menu_fm, text='Product', font=('Bold', 20), bd=0, bg='green', fg='white',
                              activebackground='green', activeforeground='white')
    produc_button.place(x=20, y=80)
    menu_button = tk.Button(toggle_menu_fm, text='Menu', font=('Bold', 20), bd=0, bg='green', fg='white',
                            activebackground='green', activeforeground='white')
    menu_button.place(x=20, y=140)
    profile_button = tk.Button(toggle_menu_fm, text='profile', font=('Bold', 20), bd=0, bg='green', fg='white',
                               activebackground='green', activeforeground='white')
    profile_button.place(x=20, y=200)

    def toggle_profile():
        def collapse_toggle_profile():
            toggle_profile_fm.destroy()
            toggle_profile.config(text='--')
            toggle_profile.config(command=toggle_profile)

        toggle_profile_fm = tk.Frame(toggle_menu_fm, bg='green')
        toggle_profile_fm.place(x=0, y=50, height=500, width=200)

        def image_profile():
            image_path = "favicon.ico"
            image = tk.PhotoImage(file=image_path)
            image_label.pack()
            image_label = tk.Label(image_profile, image=image).place(x=50, y=250)
            toggle_button.config(text='-')
            toggle_button.config(command=collapse_toggle_profile)
            toggle_button.config(text='X')
            toggle_button.config(command=colapse_toggle_menu)

    toggle_button = tk.Button(layar_frame, text='=', bg='green', fg='white', font=('Bold', 20), bd=0,
                              activebackground='green', activeforeground='white', command=toggle_menu)
    toggle_button.pack(side=tk.LEFT)
    title_lb = tk.Label(layar_frame, text='Tkinter menu', bg='green', fg='white', font=('Bold', 20))
    title_lb.pack(side=tk.LEFT)

layar = tk.Tk()
layar.geometry('500x500')
layar_frame = tk.Frame(layar, bg='green', highlightbackground='white', highlightthickness=1)
layar_frame.pack(side=tk.TOP, fill=tk.X)
layar_frame.pack_propagate(False)
layar_frame.configure(height=50)

data1 = {'Country': ['A', 'B', 'C', 'D', 'E'],
         'gdp_per_capita': [45000, 42000, 52000, 49000, 47000]
         }
df1 = pd.DataFrame(data1)

figure1 = plt.Figure(figsize=(6, 5), dpi=500)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, layar_frame)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df1[['Country', 'gdp_per_capita']].groupby('Country').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')

toggle_menu()

layar.mainloop()
