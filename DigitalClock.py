# ==========================DIGITAL CLOCK=======================================
import tkinter as tk
from tkinter import Label
import time
import colorsys

def update_time():
    # Get the current time
    current_time = time.strftime('%I:%M:%S %p')
    
    # Update the labels with the current time
    time_label.config(text=current_time)
    
    # Get the current second and convert it to a hue value
    second = int(time.strftime('%S'))
    hue = second / 60.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)

    # Convert the RGB values to a format tkinter can use
    rgb_color = '#%02x%02x%02x' % (int(r*255), int(g*255), int(b*255))

    # Set the color of the time label
    time_label.config(fg='Black',bg=rgb_color)

    # Schedule the function to be called again after 1000 milliseconds (1 second)
    time_label.after(1, update_time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create and place the time label
time_label = Label(root, font=('calibri', 100,'bold'))
time_label.pack()

# Call the update_time function to start the clock
update_time()

# Run the main loop
root.mainloop()

