# Kode Python
import tkinter as tk
import serial

# Inisialisasi serial port
serialPort = serial.Serial('COM3', 57600)  # Ganti dengan port yang sesuai

def read_serial():
    if serialPort.in_waiting > 0:
        try:
            line = serialPort.readline().decode('utf-8').rstrip()
            infrared_label.config(text=line)
        except UnicodeDecodeError:
            print("UnicodeDecodeError: Skipping invalid byte")
    infrared_label.after(100, read_serial)

# Fungsi untuk menghentikan program
def quit_program():
    serialPort.close()
    root.destroy()

# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Output Sensor Inframerah")
root.geometry("200x100")

# Label untuk menampilkan output
infrared_label = tk.Label(root, text="Tidak Ada Api")
infrared_label.pack(pady=20)

# Tombol untuk keluar
quit_button = tk.Button(root, text="Quit", command=quit_program)
quit_button.pack()

# Membaca data serial
read_serial()

# Menjalankan GUI
root.mainloop()
