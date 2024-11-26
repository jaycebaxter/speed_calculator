#################################################################################
# Program: Speed Calculator
# Author: Jayce Baxter
# Date: November 24th, 2024
# Description: Allows the user to input the speed they're driving vs how fast 
#              they should be driving
#################################################################################

# Importing everything I need
from tkinter import *
from tkinter import ttk

# Defines a function that I can use to store the speeds in a variable
def submit_current_speed():
    speed1 = current_speed.get()

def submit_desired_speed():
    speed2 = desired_speed.get()

# Initializes the window
main_window = Tk()

# Title of the window
main_window.title("Speed Calculator")

# Size of the window
main_window.geometry("400x600")

# Adds a label for the entry box current_speed
current_speed_label = Label(main_window, text = "Enter the current speed")
current_speed_label.pack()
current_speed_label.place(relx = 0.5, rely = 0.05, anchor = 'center')

# Adds an entry box for current_speed
current_speed = Entry(main_window)
current_speed.pack()
current_speed.place(relx = 0.5, rely = 0.1, anchor = 'center')

# Adds a button to submit the current_speed
current_speed_submit = Button(
    current_speed,
    text = "Submit",
    padx = 0.5,
    pady = 0.5,
    command = submit_current_speed,
    anchor = 'center').pack()

# Adds a label for the entry box desired_speed
desired_speed_label = Label(main_window, text = "Enter your desired speed")
desired_speed_label.pack()
desired_speed_label.place(relx = 0.5, rely = 0.2, anchor = 'center')

# Adds an entry box for desired_speed
desired_speed = Entry(main_window)
desired_speed.pack()
desired_speed.place(relx = 0.5, rely = 0.25, anchor = 'center')

# Runs the window
main_window.mainloop()