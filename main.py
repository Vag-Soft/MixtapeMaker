import json
import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

# Prompts the user to select a file and returns its path
def select_file(image_input):
    Tk().withdraw()
    file_path = askopenfilename()
    image_input.delete(0, tk.END)
    image_input.insert(0, file_path)

# Prompts the user to select a folder and returns its path
def select_folder(audio_input):
    Tk().withdraw()
    folder_path = askdirectory()
    audio_input.delete(0, tk.END)
    audio_input.insert(0, folder_path)

# Saves the current settings
def save_settings(root):
    # Creates a dictionary with all the current selected settings in the gui
    settings_dict = {
        'image_file': root.nametowidget("image_frame").nametowidget('image_input').get(),
        'audio_folder': root.children.get('audio_frame').nametowidget('audio_input').get(),
        'save_folder': root.children.get('save_frame').nametowidget('save_input').get(),
        'width': root.children.get('vidsets_frame').nametowidget('width_input').get(),
        'height': root.children.get('vidsets_frame').nametowidget('height_input').get(),
        'fps': root.children.get('vidsets_frame').nametowidget('fps_input').get(),
        'fade_in_secs': root.children.get('audiosets_frame').nametowidget('audiofadein_input').get(),
        'fade_out_secs': root.children.get('audiosets_frame').nametowidget('audiofadeout_input').get(),
        'per_file': root.children.get('audiosets_frame').nametowidget('perfile_input').state(),
        'max_hours': root.children.get('extrasets_frame').nametowidget('hours_input').get(),
        'max_mins': root.children.get('extrasets_frame').nametowidget('mins_input').get(),
        'max_secs': root.children.get('extrasets_frame').nametowidget('secs_input').get(),
        'threads': root.children.get('extrasets_frame').nametowidget('threads_input').get()
    }

    # Opens a file and writes the dictionary into it
    with open('settings.json', 'w') as file:
        json.dump(settings_dict, file)

    print("Settings saved successfully.")

# Loads the settings
def load_settings():
    # Tries to open a file to load the settings and return them
    try:
        with open('settings.json', 'r') as file:
            settings_dict = json.load(file)
        print("Settings loaded successfully.")
        return settings_dict
    except FileNotFoundError:
        print("No settings file found.")
        return
    except json.JSONDecodeError:
        print("Error decoding the settings file")
        return


# Exports the video
def export_video(root):
    save_settings(root)
    return

# Creates a frame for the image input area
def create_image_frame(root, settings):
    image_frame = tk.Frame(root, name="image_frame")
    image_frame.pack(pady=10)

    image_label = tk.Label(image_frame, text="Select your image")
    image_label.pack(side=tk.TOP, anchor='w')

    image_input = tk.Entry(image_frame, width=50, name="image_input")
    image_input.insert(0, settings.get('image_file'))
    image_input.pack(side=tk.LEFT, padx=5)

    image_button = tk.Button(image_frame, text="Explore", command=lambda: select_file(image_input))
    image_button.pack(side=tk.LEFT, padx=5)

# Creates a frame for the audio input area
def create_audio_frame(root, settings):
    audio_frame = tk.Frame(root, name="audio_frame")
    audio_frame.pack(pady=10)

    audio_label = tk.Label(audio_frame, text="Select your audio folder")
    audio_label.pack(side=tk.TOP, anchor='w')

    audio_input = tk.Entry(audio_frame, width=50, name="audio_input")
    audio_input.insert(0, settings.get('audio_folder'))
    audio_input.pack(side=tk.LEFT, padx=5)

    audio_button = tk.Button(audio_frame, text="Explore", command=lambda: select_folder(audio_input))
    audio_button.pack(side=tk.LEFT, padx=5)

# Creates a frame for the save input area
def create_save_frame(root, settings):
    save_frame = tk.Frame(root, name="save_frame")
    save_frame.pack(pady=10)

    save_label = tk.Label(save_frame, text="Select your save folder")
    save_label.pack(side=tk.TOP, anchor='w')

    save_input = tk.Entry(save_frame, width=50, name="save_input")
    save_input.insert(0, settings.get('save_folder'))
    save_input.pack(side=tk.LEFT, padx=5)

    save_button = tk.Button(save_frame, text="Explore", command=lambda: select_folder(save_input))
    save_button.pack(side=tk.LEFT, padx=5)

# Creates a frame for the video settings area
def create_vidsets_frame(root, settings):
    vidsets_frame = tk.Frame(root, name="vidsets_frame")
    vidsets_frame.pack(pady=5)

    vidsets_label = tk.Label(vidsets_frame, text="Video Settings")
    vidsets_label.pack(side=tk.TOP, anchor='w', pady=10)

    width_label = tk.Label(vidsets_frame, text="Width")
    width_label.pack(side=tk.LEFT, anchor='w')

    width_input = tk.Entry(vidsets_frame, width=5, justify="center", name="width_input")
    width_input.insert(0, settings.get('width'))
    width_input.pack(side=tk.LEFT, padx=5)

    height_label = tk.Label(vidsets_frame, text="Height")
    height_label.pack(side=tk.LEFT, anchor='w')

    height_input = tk.Entry(vidsets_frame, width=5, justify="center", name="height_input")
    height_input.insert(0, settings.get('height'))
    height_input.pack(side=tk.LEFT, padx=5)

    fps_label = tk.Label(vidsets_frame, text="FPS")
    fps_label.pack(side=tk.LEFT, anchor='w')

    fps_input = tk.Entry(vidsets_frame, width=4, justify="center", name="fps_input")
    fps_input.insert(0, settings.get('fps'))
    fps_input.pack(side=tk.LEFT, padx=5)

# Creates a frame for the audio settings area
def create_audiosets_frame(root, settings):
    audiosets_frame = tk.Frame(root, name="audiosets_frame")
    audiosets_frame.pack(pady=5)

    audiosets_label = tk.Label(audiosets_frame, text="Audio Settings")
    audiosets_label.pack(side=tk.TOP, anchor='w', pady=10)

    audiofadein_label = tk.Label(audiosets_frame, text="Fade-In Secs")
    audiofadein_label.pack(side=tk.LEFT, anchor='w')

    audiofadein_input = tk.Entry(audiosets_frame, width=4, justify="center", name="audiofadein_input")
    audiofadein_input.insert(0, settings.get('fade_in_secs'))
    audiofadein_input.pack(side=tk.LEFT, padx=5)

    audiofadeout_label = tk.Label(audiosets_frame, text="Fade-Out Secs")
    audiofadeout_label.pack(side=tk.LEFT, anchor='w')

    audiofadeout_input = tk.Entry(audiosets_frame, width=4, justify="center", name="audiofadeout_input")
    audiofadeout_input.insert(0, settings.get('fade_out_secs'))
    audiofadeout_input.pack(side=tk.LEFT, padx=5)

    perfile_label = tk.Label(audiosets_frame, text="Per File")
    perfile_label.pack(side=tk.LEFT, anchor='w')

    perfile_input = ttk.Checkbutton(audiosets_frame, name="perfile_input")
    perfile_input.state(['!alternate'])
    perfile_input.state(settings.get('per_file'))
    perfile_input.pack(side=tk.LEFT, padx=1)

# Creates a frame for the extra settings area
def create_extrasets_frame(root, settings):
    extrasets_frame = tk.Frame(root, name="extrasets_frame")
    extrasets_frame.pack(pady=5)

    extrasets_label = tk.Label(extrasets_frame, text="Extra Settings")
    extrasets_label.pack(side=tk.TOP, anchor='w', pady=10)

    max_dur_label = tk.Label(extrasets_frame, text="Max Duration Part")
    max_dur_label.pack(side=tk.LEFT, anchor='w')

    hours_label = tk.Label(extrasets_frame, text="H")
    hours_label.pack(side=tk.LEFT, anchor='w')

    hours_input = tk.Entry(extrasets_frame, width=4, justify="center", name="hours_input")
    hours_input.insert(0, settings.get('max_hours'))
    hours_input.pack(side=tk.LEFT, padx=5)

    mins_label = tk.Label(extrasets_frame, text="M")
    mins_label.pack(side=tk.LEFT, anchor='w')

    mins_input = tk.Entry(extrasets_frame, width=4, justify="center", name="mins_input")
    mins_input.insert(0, settings.get('max_mins'))
    mins_input.pack(side=tk.LEFT, padx=5)

    secs_label = tk.Label(extrasets_frame, text="S")
    secs_label.pack(side=tk.LEFT, anchor='w')

    secs_input = tk.Entry(extrasets_frame, width=4, justify="center", name="secs_input")
    secs_input.insert(0, settings.get('max_secs'))
    secs_input.pack(side=tk.LEFT, padx=5)

    threads_label = tk.Label(extrasets_frame, text="Threads")
    threads_label.pack(side=tk.LEFT, anchor='w')

    threads_input = tk.Entry(extrasets_frame, width=4, justify="center", name="threads_input")
    threads_input.insert(0, settings.get('threads'))
    threads_input.pack(side=tk.LEFT, padx=5)

# Creates a frame for the extra settings area
def create_export_frame(root, settings):
    export_frame = tk.Frame(root, name="export_frame")
    export_frame.pack(pady=5)

    export_button = tk.Button(export_frame, text="Export", command=lambda: export_video(root))
    export_button.pack(side=tk.RIGHT, padx=5)

def run_gui():
    # Loads the settings from the last session
    settings = load_settings()

    # Creates the main window
    root = tk.Tk()
    root.title("MixtapeMaker")

    # Creates a frame for the image input area
    create_image_frame(root, settings)
    # Creates a frame for the audio input area
    create_audio_frame(root, settings)
    # Creates a frame for the save input area
    create_save_frame(root, settings)
    # Creates a frame for the video settings area
    create_vidsets_frame(root, settings)
    # Creates a frame for the audio settings area
    create_audiosets_frame(root, settings)
    # Creates a frame for the extra settings area
    create_extrasets_frame(root, settings)
    # Creates a frame for the export area
    create_export_frame(root, settings)


    # Runs the application
    root.mainloop()

if __name__ == "__main__":
    run_gui()