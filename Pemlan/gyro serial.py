import tkinter as tk
import serial

# Buat objek Serial untuk berkomunikasi dengan Arduino
arduino = serial.Serial('COM3', 57600, timeout=1)  # Ganti 'COM3' dengan port serial yang digunakan
threshold = 0.2
def read_serial_data():
    # Baca data dari Arduino
    data = arduino.readline().decode().strip()
    data1, data2, data3 = data.split(',')
    # Update label dengan data yang diterima
    data_label.config(text=f"Kemiringan X: {data1} dan Kemiringan Y: {data2}")
    # Cek kondisi sensor dan kontrol buzzer
    angle = float(data1)
    if angle > threshold:
        arduino.write(b'1')  # Kirim sinyal ke Arduino untuk menghidupkan buzzer
    else:
        arduino.write(b'0')  # Kirim sinyal ke Arduino untuk mematikan buzzer
    # Jalankan fungsi ini lagi setelah 500ms
    root.after(500, read_serial_data)

def on_exit():
    # Matikan buzzer dan tutup koneksi serial saat aplikasi keluar
    arduino.write(b'0')  # Kirim sinyal ke Arduino untuk mematikan buzzer
    arduino.close()
    root.destroy()

# Buat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Output Arduino")
root.geometry("300x200")

# Buat label untuk menampilkan data
data_label = tk.Label(root, text="", font=("Arial", 16))
data_label.pack(pady=50)

read_serial_data()

# Jalankan fungsi on_exit() saat aplikasi ditutup
root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()