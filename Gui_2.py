
import tkinter as tk
from tkinter import ttk
import subprocess
import os
import signal

# Global variable to hold the subprocess object
process = None

def Breakbeam_script():
    global process
    try:
        # Execute your script here
        process = subprocess.Popen(["/home/YCCap/ballmap/./blue.sh"], shell=True)   #process = subprocess.Popen(["python", "Breakbeamtest.py"])  # Replace "your_script.py" with the name of your script
    except Exception as e:
        print(f"Error running script: {e}")
        
def stopBreakbeam_script():
    global process
    try:
        # Terminate the subprocess if it's running
        if process:
            os.kill(process.pid, signal.SIGTERM)
            process = None 
            print("Subprocess terminated.")
    except Exception as e:
        print(f"Error stopping script: {e}")
        
        
def Red_Ball_Buttons(root):
    additional_window = tk.Toplevel(root)
    additional_window.title("Red Ball")
    additional_window.attributes("-fullscreen",False)
    
    # Configure style for blue accents
    style = ttk.Style()
    style.configure("Blue.TButton", foreground="blue", background="light blue")
    
    # Create a label
    label = tk.Label(additional_window, text="Click the button to run the script", font=("Arial", 12))
    label.pack(pady=20)
    
    def go_back():
        additional_window.destroy()

    button1 = tk.Button(additional_window, text="Start", command=Breakbeam_script)
    button1.pack()

    button2 = tk.Button(additional_window, text="Stop", command=stopBreakbeam_script)
    button2.pack()

    back_button = tk.Button(additional_window, text="Back", command=go_back)
    back_button.pack()

def Blue_Ball_Buttons(root):
    additional_window = tk.Toplevel(root)
    additional_window.title("Blue Ball")
    additional_window.attributes("-fullscreen", False)
    
    # Configure style for blue accents
    style = ttk.Style()
    style.configure("Blue.TButton", foreground="blue", background="light blue")
    
    # Create a label
    label = tk.Label(additional_window, text="Click the button to run the script", font=("Arial", 12))
    label.pack(pady=20)
    
    
    def go_back():
        additional_window.destroy()

    button1 = tk.Button(additional_window, text="Start", command=Breakbeam_script)
    button1.pack()

    button2 = tk.Button(additional_window, text="Stop", command=stopBreakbeam_script)
    button2.pack()

    back_button = tk.Button(additional_window, text="Back", command=go_back)
    back_button.pack()

# Create the main window
def create_gui():
    root = tk.Tk()
    root.title("YC Ballmap")
    root.attributes("-fullscreen", False)
    
    # Configure style for blue accents
    style = ttk.Style()
    style.configure("Blue.TButton", foreground="blue", background="light blue")

    # Create a label
    label = tk.Label(root, text="Choose the ball you are mapping", font=("Arial", 12))
    label.pack(pady=20)

    # Button to show additional buttons
    red_ball_button = ttk.Button(root, text="Red Ball", command=lambda: Red_Ball_Buttons(root))
    red_ball_button.pack()

    blue_ball_button = ttk.Button(root, text="Blue Ball", command=lambda: Blue_Ball_Buttons(root))
    blue_ball_button.pack()

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()


