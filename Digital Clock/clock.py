# Importing the libraries
import tkinter as tk
import time

def update_clock():
    # Get the current system time formatted as Hours:Minutes:Seconds (24-hour format)
    current_time = time.strftime("%H:%M:%S")
    
    # Update the label widget's text with the formatted time string
    clock_label.config(text=current_time)
    
    # Schedule this function to run again after 1000 milliseconds (1 second)
    clock_label.after(1000, update_clock)

# Initialize the main window application
window = tk.Tk()
window.title("Digital Clock")

# Create a text label widget styled to look like a digital clock screen
clock_label = tk.Label(
    window, 
    font=("Helvetica", 48), 
    bg="black", 
    fg="cyan"
)

# Apply padding and add the label widget into the window frame
clock_label.pack(padx=20, pady=20)

# Trigger the initial time update cycle
update_clock()

# Start the Tkinter event loop to keep the window open and interactive
window.mainloop()