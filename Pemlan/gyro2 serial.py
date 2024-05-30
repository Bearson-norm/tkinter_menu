import tkinter as tk
import serial

# Buat objek Serial untuk berkomunikasi dengan Arduino
arduino = serial.Serial('COM3', 57600, timeout=1)  # Ganti 'COM3' sesuai dengan port serial yang digunakan

def read_serial_data():
    # Baca data dari Arduino
    data = arduino.readline().decode().strip()
    #data1, data2 = data.split(',')
    # Update label dengan data yang diterima
    data_label.config(text=data)
    # Jalankan fungsi ini lagi setelah 50ms
    root.after(500, read_serial_data)

def on_exit():
    # Tutup koneksi serial saat aplikasi keluar
    arduino.close()
    root.destroy()

# Buat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Output Arduino")
root.geometry("1000x200")

# Buat label untuk menampilkan data
data_label = tk.Label(root, text="", font=("Arial", 16))
data_label.pack(pady=50)

# Baca data dari Arduino setiap 50ms
root.after(500, read_serial_data)

# Jalankan fungsi on_exit() saat aplikasi ditutup
root.protocol("WM_DELETE_WINDOW", on_exit)

# Jalankan aplikasi Tkinter
root.mainloop()
