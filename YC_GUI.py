import tkinter as tk
from tkinter import ttk
import subprocess

# Global variable to hold the subprocess object
process = None

def run_script():
    global process
    try:
        # Execute your script here
        process = subprocess.Popen(["python", "Breakbeamtest.py"])  # Replace "your_script.py" with the name of your script
    except Exception as e:
        print(f"Error running script: {e}")

def stop_script():
    global process
    try:
        # Terminate the subprocess if it's running
        if process:
            process.terminate()
    except Exception as e:
        print(f"Error stopping script: {e}")

def create_gui():
    root = tk.Tk()
    root.title("YC Ballmap")
    root.attributes("-fullscreen", True)  # Set window to fullscreen

    # Configure style for blue accents
    style = ttk.Style()
    style.configure("Blue.TButton", foreground="blue", background="light blue")

    # Create a label
    label = tk.Label(root, text="Click the button to run the script", font=("Arial", 12))
    label.pack(pady=20)

    # Create a button to run the script
    start_button = ttk.Button(root, text="Start", style="Blue.TButton", command=run_script)
    start_button.pack()

    # Create a button to stop the script
    stop_button = ttk.Button(root, text="Stop", style="Blue.TButton", command=stop_script)
    stop_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()






