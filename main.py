import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

# Prompts the user to select a file and returns its path
def select_file(image_input):
    Tk().withdraw()
    file_path = askopenfilename()
    image_input.insert(0, file_path)

# Prompts the user to select a folder and returns its path
def select_folder(audio_input):
    Tk().withdraw()
    folder_path = askdirectory()
    audio_input.insert(0, folder_path)


def run_gui():
    # Creates the main window
    root = tk.Tk()
    root.title("MixtapeMaker")

    # Creates a frame for the image input area
    image_frame = tk.Frame(root)
    image_frame.pack(pady=10)

    image_label = tk.Label(image_frame, text="Select your image")
    image_label.pack(side=tk.TOP, anchor='w')

    image_input = tk.Entry(image_frame, width=50)
    image_input.pack(side=tk.LEFT, padx=5)

    image_button = tk.Button(image_frame, text="Explore", command=lambda: select_file(image_input))
    image_button.pack(side=tk.LEFT, padx=5)

    # Creates a frame for the audio input area
    audio_frame = tk.Frame(root)
    audio_frame.pack(pady=10)

    audio_label = tk.Label(audio_frame, text="Select your audio folder")
    audio_label.pack(side=tk.TOP, anchor='w')

    audio_input = tk.Entry(audio_frame, width=50)
    audio_input.pack(side=tk.LEFT, padx=5)

    audio_button = tk.Button(audio_frame, text="Explore", command=lambda: select_folder(audio_input))
    audio_button.pack(side=tk.LEFT, padx=5)

    # Runs the application
    root.mainloop()

if __name__ == "__main__":
    run_gui()