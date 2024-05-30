import serial
from tkinter import *

def read_serial():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(data)  # Menampilkan data ke konsol
            text.insert(END, data + "\n")  # Menambahkan data ke Tkinter Text widget
            text.see(END)  # Menggulirkan ke bawah saat ada data baru

def close_serial():
    ser.close()

# Membuat objek serial
ser = serial.Serial('COM6', 9600)  # Ubah 'COM3' dengan port serial Arduino yang sesuai

# Membuat GUI Tkinter
root = Tk()
root.title("Ultrasonic Sensor")
root.geometry("400x300")

# Membuat Text widget untuk menampilkan data
text = Text(root)
text.pack()

# Membuat tombol Close
close_button = Button(root, text="Close", command=close_serial)
close_button.pack()

# Membaca data serial dalam thread terpisah
from threading import Thread
serial_thread = Thread(target=read_serial)
serial_thread.daemon = True
serial_thread.start()

root.mainloop()
