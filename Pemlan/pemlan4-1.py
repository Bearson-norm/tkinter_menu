import tkinter as tk
from PIL import ImageTk, Image

def show_image():
    # Create a new window
    image_window = tk.Toplevel(root)
    
    # Load the image
    image = Image.open("pemlan2.jpeg")
    photo = ImageTk.PhotoImage(image)
    
    # Display the image in a label
    image_label = tk.Label(image_window, image=photo)
    image_label.pack()
    
    # Set the title of the window
    image_window.title("Image Viewer")
    
    # Run the main event loop for the image window
    image_window.mainloop()

# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("Image Button")

# Create a button
button = tk.Button(root, text="Show Image", command=show_image)
button.pack()

# Run the main event loop
root.mainloop()
