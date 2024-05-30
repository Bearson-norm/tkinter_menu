import tkinter as tk
import matplotlib.pyplot as plt

# Sample data for the graph
x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 2, 8]

# Function to generate content for each page
def generate_content(page_name):
  content = tk.Frame(window)
  if page_name == "menu":
    content.config(bg="lightblue")
    label = tk.Label(content, text="This is the Menu Page")
    label.pack()
  elif page_name == "profile":
    content.config(bg="lightgreen")
    label = tk.Label(content, text="Your Profile Information")
    label.pack()
  elif page_name == "graph":
    content.config(bg="lightyellow")
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='X', ylabel='Y', title='Sample Graph')
    canvas = plt.get_current_fig_manager().canvas
    canvas.draw()

    # Option 1: Pack the canvas directly (preferred)
    # content.pack(fill=tk.BOTH, expand=True)

    # Option 2: Use a container frame with desired size
    canvas_container = tk.Frame(content, width=500, height=300)
    canvas_container.pack()
    canvas_widget = canvas.get_tk_widget()  # Get the Tkinter widget for the canvas
    canvas_widget.pack(fill=tk.BOTH, expand=True)
  content.pack(fill=tk.BOTH, expand=True)
  return content

# Function to toggle the menu visibility
def toggle_menu():
  global menu_open
  if menu_open:
    menu_button.config(text="<< Menu")
    menu_frame.pack_forget()
  else:
    menu_button.config(text=">> Menu")
    menu_frame.pack(fill=tk.Y, expand=True)
  menu_open = not menu_open

# Initialize variables
window = tk.Tk()
window.title("Collapsible Menu App")
window.geometry("500x500")
menu_open = False

# Create the menu frame
menu_frame = tk.Frame(window)

# Create menu buttons
menu_button = tk.Button(menu_frame, text=">> Menu", command=toggle_menu)
menu_button.pack(pady=10)
menu_button_menu = tk.Button(menu_frame, text="Menu", command=lambda: generate_content("menu"))
menu_button_menu.pack(pady=5)
menu_button_profile = tk.Button(menu_frame, text="Profile", command=lambda: generate_content("profile"))
menu_button_profile.pack(pady=5)
menu_button_graph = tk.Button(menu_frame, text="Graph", command=lambda: generate_content("graph"))
menu_button_graph.pack(pady=5)

# Create the initial content frame (empty)
content_frame = generate_content("")

# Display everything
menu_frame.pack(fill=tk.Y, expand=True)
content_frame.pack(fill=tk.BOTH, expand=True)

window.mainloop()
