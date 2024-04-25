# import tkinter as tk
# from tkinter import ttk
# import subprocess
# import threading

# # Global variables
# process = None
# output_text = None

# def print_and_write_to_text(text):
    # global output_text
    # print(text)  # Print to terminal
    # output_text.config(state=tk.NORMAL)  # Enable editing
    # output_text.insert(tk.END, text)  # Insert text without newline
    # output_text.config(state=tk.DISABLED)  # Disable editing
    # output_text.yview(tk.END)  # Scroll to the end

# def Breakbeam_script():
    # global process
    # try:
        # # Execute your script here
        # print_and_write_to_text("Attempting to start subprocess...\n")
        # process = subprocess.Popen(["/home/YCCap/ballmap/./blue.sh"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # print_and_write_to_text("Subprocess started successfully.\n")
        
        # # Start a separate thread to read and display output
        # threading.Thread(target=read_output).start()
    # except Exception as e:
        # print_and_write_to_text(f"Error running script: {e}\n")

# def stopBreakbeam_script():
    # global process
    # try:
        # # Terminate the subprocess if it's running
        # if process:
            # process.terminate()
            # process = None 
            # print_and_write_to_text("Subprocess terminated.\n")
    # except Exception as e:
        # print_and_write_to_text(f"Error stopping script: {e}\n")

# def read_output():
    # global process
    # while True:
        # line = process.stdout.readline()
        # if not line:
            # break
        # print_and_write_to_text(line.decode("utf-8"))  # Convert bytes to string and print

# def Red_Ball_Buttons(root):
    # additional_window = tk.Toplevel(root)
    # additional_window.title("Red Ball")
    # additional_window.attributes("-fullscreen", True)
    
    # # Create a label
    # label = tk.Label(additional_window, text="Click the button to run the script", font=("Arial", 12))
    # label.pack(pady=20)
    
    # # Create a Text widget to display output
    # global output_text
    # output_text = tk.Text(additional_window, wrap=tk.NONE, height=3, width=50)
    # output_text.pack(pady=10, padx=10)
    # output_text.config(state=tk.DISABLED)  # Make it read-only
    
    # def go_back():
        # additional_window.destroy()

    # button1 = tk.Button(additional_window, text="Start", command=Breakbeam_script, width=10)
    # button1.pack()

    # button2 = tk.Button(additional_window, text="Stop", command=stopBreakbeam_script, width=10)
    # button2.pack()

    # back_button = tk.Button(additional_window, text="Back", command=go_back, width=10)
    # back_button.pack()

# def Blue_Ball_Buttons(root):
    # additional_window = tk.Toplevel(root)
    # additional_window.title("Blue Ball")
    # additional_window.attributes("-fullscreen", True)
    
    # # Create a label
    # label = tk.Label(additional_window, text="Click the button to run the script", font=("Arial", 12))
    # label.pack(pady=20)
    
    # # Create a Text widget to display output
    # global output_text
    # output_text = tk.Text(additional_window, wrap=tk.NONE, height=3, width=50)
    # output_text.pack(pady=10, padx=10)
    # output_text.config(state=tk.DISABLED)  # Make it read-only
    
    # def go_back():
        # additional_window.destroy()

    # button1 = tk.Button(additional_window, text="Start", command=Breakbeam_script, width=10)
    # button1.pack()

    # button2 = tk.Button(additional_window, text="Stop", command=stopBreakbeam_script, width=10)
    # button2.pack()

    # back_button = tk.Button(additional_window, text="Back", command=go_back, width=10)
    # back_button.pack()

# # Exit the program
# def exit_program(root):
    # root.destroy()

# # Create the main window
# def create_gui():
    # root = tk.Tk()
    # root.title("YC Ballmap")
    # root.attributes("-fullscreen", True)

    # # Create a label
    # label = tk.Label(root, text="Choose the ball you are mapping", font=("Arial", 12))
    # label.pack(pady=20)

    # # Button to show additional buttons
    # red_ball_button = ttk.Button(root, text="Red Ball", command=lambda: Red_Ball_Buttons(root), width=20)
    # red_ball_button.pack()

    # blue_ball_button = ttk.Button(root, text="Blue Ball", command=lambda: Blue_Ball_Buttons(root), width=20)
    # blue_ball_button.pack()

    # # Exit button
    # exit_button = ttk.Button(root, text="Exit Program", command=lambda: exit_program(root), width=20)
    # exit_button.pack()

    # # Start the main event loop
    # root.mainloop()

# if __name__ == "__main__":
    # create_gui()

import tkinter as tk
from tkinter import ttk
import os
import threading

# Global variables
process = None
output_text = None

def print_and_write_to_text(text):
    global output_text
    print(text)  # Print to terminal
    output_text.config(state=tk.NORMAL)  # Enable editing
    output_text.insert(tk.END, text)  # Insert text without newline
    output_text.config(state=tk.DISABLED)  # Disable editing
    output_text.yview(tk.END)  # Scroll to the end

def BLUE_script():
    global process
    try:
        # Execute your script here
        print_and_write_to_text("Attempting to start subprocess...\n")
        process = os.popen("/home/YCCap/ballmap/./blue.sh")
        print_and_write_to_text("Subprocess started successfully.\n")
        
        # Start a separate thread to read and display output
        threading.Thread(target=read_output).start()
    except Exception as e:
        print_and_write_to_text(f"Error running script: {e}\n")

def stopBLUE_script():
    global process
    try:
        # Terminate the subprocess if it's running
        if process:
            process.terminate()
            process = None 
            print_and_write_to_text("Subprocess terminated.\n")
    except Exception as e:
        print_and_write_to_text(f"Error stopping script: {e}\n")



def RED_script():
    global process
    try:
        # Execute your script here
        print_and_write_to_text("Attempting to start subprocess...\n")
        process = os.popen("/home/YCCap/ballmap/./run.sh")
        print_and_write_to_text("Subprocess started successfully.\n")
        
        # Start a separate thread to read and display output
        threading.Thread(target=read_output).start()
    except Exception as e:
        print_and_write_to_text(f"Error running script: {e}\n")

def stopRED_script():
    global process
    try:
        # Terminate the subprocess if it's running
        if process:
            process.terminate()
            process = None 
            print_and_write_to_text("Subprocess terminated.\n")
    except Exception as e:
        print_and_write_to_text(f"Error stopping script: {e}\n")


def read_output():
    global process
    while True:
        line = process.readline()
        if not line:
            break
        print_and_write_to_text(line)

def Red_Ball_Buttons(root):
    additional_window = tk.Toplevel(root)
    additional_window.title("Red Ball")
    additional_window.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  # Set fullscreen
    additional_window.attributes("-zoomed", True)  # Maximize window on Windows
    
    # Create a label
    label = tk.Label(additional_window, text="Click the button to run the script", font=("Arial", 12))
    label.pack(pady=20, anchor="center")
    
    # Create a Text widget to display output
    global output_text
    output_text = tk.Text(additional_window, wrap=tk.NONE, height=3, width=50)
    output_text.pack(pady=10, padx=10, anchor="center")
    output_text.config(state=tk.DISABLED)  # Make it read-only
    
    def go_back():
        additional_window.destroy()

    button1 = tk.Button(additional_window, text="Start", command=RED_script, width=10)
    button1.pack(pady=5, anchor="center")

    button2 = tk.Button(additional_window, text="Stop", command=stopRED_script, width=10)
    button2.pack(pady=5, anchor="center")

    back_button = tk.Button(additional_window, text="Back", command=go_back, width=10)
    back_button.pack(pady=5, anchor="center")

def Blue_Ball_Buttons(root):
    additional_window = tk.Toplevel(root)
    additional_window.title("Blue Ball")
    additional_window.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  # Set fullscreen
    additional_window.attributes("-zoomed", True)  # Maximize window on Windows
    
    # Create a label
    label = tk.Label(additional_window, text="Click the button to run the script", font=("Arial", 12))
    label.pack(pady=20, anchor="center")
    
    # Create a Text widget to display output
    global output_text
    output_text = tk.Text(additional_window, wrap=tk.NONE, height=3, width=50)
    output_text.pack(pady=10, padx=10, anchor="center")
    output_text.config(state=tk.DISABLED)  # Make it read-only
    
    def go_back():
        additional_window.destroy()

    button1 = tk.Button(additional_window, text="Start", command=BLUE_script, width=10)
    button1.pack(pady=5, anchor="center")

    button2 = tk.Button(additional_window, text="Stop", command=stopBLUE_script, width=10)
    button2.pack(pady=5, anchor="center")

    back_button = tk.Button(additional_window, text="Back", command=go_back, width=10)
    back_button.pack(pady=5, anchor="center")

# Exit the program
def exit_program(root):
    root.destroy()

# Create the main window
def create_gui():
    root = tk.Tk()
    root.title("YC Ballmap")
    root.attributes("-fullscreen", True)

    # Create a label
    label = tk.Label(root, text="Choose the ball you are mapping", font=("Arial", 12))
    label.pack(pady=20, anchor="center")

    # Button to show additional buttons
    red_ball_button = ttk.Button(root, text="Red Ball", command=lambda: Red_Ball_Buttons(root), width=20)
    red_ball_button.pack(pady=5, anchor="center")

    blue_ball_button = ttk.Button(root, text="Blue Ball", command=lambda: Blue_Ball_Buttons(root), width=20)
    blue_ball_button.pack(pady=5, anchor="center")

    # Exit button
    exit_button = ttk.Button(root, text="Exit Program", command=lambda: exit_program(root), width=20)
    exit_button.pack(pady=5, anchor="center")

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()



#attempted to get the stop button to work

# import tkinter as tk
# from tkinter import ttk
# import subprocess
# import threading
# import RPi.GPIO as GPIO
# import atexit

# # Global variables
# process = None
# output_text = None
# beam_sensor_pin = 18  # Define the GPIO pin for the break beam sensor

# def print_and_write_to_text(text):
    # global output_text
    # if '[7:41:33.728822432] [21050] INFO' not in text:
        # print(text)  # Print to terminal
        # output_text.config(state=tk.NORMAL)  # Enable editing
        # output_text.insert(tk.END, text)  # Insert text without newline
        # output_text.config(state=tk.DISABLED)  # Disable editing
        # output_text.yview(tk.END)  # Scroll to the end

# def Breakbeam_script():
    # global process
    # global beam_sensor_pin
    # try:
        # # Initialize GPIO
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(beam_sensor_pin, GPIO.IN)
        
        # # Execute your script here
        # print_and_write_to_text("Attempting to start subprocess...\n")
        # process = subprocess.Popen(["/home/YCCap/ballmap/./blue.sh"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # print_and_write_to_text("Subprocess started successfully.\n")
        
        # # Start a separate thread to read and display output
        # threading.Thread(target=read_output).start()
    # except Exception as e:
        # print_and_write_to_text(f"Error running script: {e}\n")
        # # Cleanup GPIO if an error occurs
        # GPIO.cleanup()

# def stopBreakbeam_script():
    # global process
    # try:
        # # Terminate the subprocess if it's running
        # if process:
            # process.terminate()
            # process.wait()  # Wait for the subprocess to terminate
            # process = None 
            # print_and_write_to_text("Subprocess terminated.\n")
    # except Exception as e:
        # print_and_write_to_text(f"Error stopping script: {e}\n")

# def read_output():
    # global process
    # while True:
        # line = process.stdout.readline()
        # if not line:
            # break
        # decoded_line = line.decode("utf-8")
        # if '[7:41:33.728822432] [21050] INFO' not in decoded_line:
            # print_and_write_to_text(decoded_line)

# def Red_Ball_Buttons(root):
    # additional_window = tk.Toplevel(root)
    # additional_window.title("Red Ball")
    # additional_window.attributes("-fullscreen", True)
    
    # # Create a label
    # label = tk.Label(additional_window, text="Click the button to run the script", font=("Arial", 12))
    # label.pack(pady=20)
    
    # # Create a Text widget to display output
    # global output_text
    # output_text = tk.Text(additional_window, wrap=tk.NONE, height=3, width=50)
    # output_text.pack(pady=10, padx=10)
    # output_text.config(state=tk.DISABLED)  # Make it read-only
    
    # def go_back():
        # additional_window.destroy()

    # button1 = tk.Button(additional_window, text="Start", command=Breakbeam_script, width=10)
    # button1.pack()

    # button2 = tk.Button(additional_window, text="Stop", command=stopBreakbeam_script, width=10)
    # button2.pack()

    # back_button = tk.Button(additional_window, text="Back", command=go_back, width=10)
    # back_button.pack()

# def Blue_Ball_Buttons(root):
    # additional_window = tk.Toplevel(root)
    # additional_window.title("Blue Ball")
    # additional_window.attributes("-fullscreen", True)
    
    # # Create a label
    # label = tk.Label(additional_window, text="Click the button to run the script", font=("Arial", 12))
    # label.pack(pady=20)
    
    # # Create a Text widget to display output
    # global output_text
    # output_text = tk.Text(additional_window, wrap=tk.NONE, height=3, width=50)
    # output_text.pack(pady=10, padx=10)
    # output_text.config(state=tk.DISABLED)  # Make it read-only
    
    # def go_back():
        # additional_window.destroy()

    # button1 = tk.Button(additional_window, text="Start", command=Breakbeam_script, width=10)
    # button1.pack()

    # button2 = tk.Button(additional_window, text="Stop", command=stopBreakbeam_script, width=10)
    # button2.pack()

    # back_button = tk.Button(additional_window, text="Back", command=go_back, width=10)
    # back_button.pack()

# # Exit the program
# def exit_program(root):
    # root.destroy()

# # Ensure GPIO cleanup when the script exits
# def on_exit():
    # GPIO.cleanup()

# # Create the main window
# def create_gui():
    # root = tk.Tk()
    # root.title("YC Ballmap")
    # root.attributes("-fullscreen", True)

    # # Create a label
    # label = tk.Label(root, text="Choose the ball you are mapping", font=("Arial", 12))
    # label.pack(pady=20)

    # # Button to show additional buttons
    # red_ball_button = ttk.Button(root, text="Red Ball", command=lambda: Red_Ball_Buttons(root), width=20)
    # red_ball_button.pack()

    # blue_ball_button = ttk.Button(root, text="Blue Ball", command=lambda: Blue_Ball_Buttons(root), width=20)
    # blue_ball_button.pack()

    # # Exit button
    # exit_button = ttk.Button(root, text="Exit Program", command=lambda: exit_program(root), width=20)
    # exit_button.pack()

    # # Register the cleanup function
    # atexit.register(on_exit)

    # # Start the main event loop
    # root.mainloop()

# if __name__ == "__main__":
    # create_gui()
