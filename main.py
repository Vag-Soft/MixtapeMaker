import json
import os

from PIL import Image

from pathvalidate import is_valid_filename

import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

from idlelib.tooltip import Hovertip

from moviepy.audio.AudioClip import concatenate_audioclips
from moviepy.audio.fx.all import audio_fadein
from moviepy.audio.fx.all import audio_fadeout
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip


# Prompts the user to select a file and returns its path
def select_file(image_input):
    # Prompts the user
    Tk().withdraw()
    file_path = askopenfilename()
    # Clears the entry box
    image_input.delete(0, tk.END)
    # Inserts the chosen path to the entry box
    image_input.insert(0, file_path)

# Prompts the user to select a folder and returns its path
def select_folder(audio_input):
    # Prompts the user
    Tk().withdraw()
    folder_path = askdirectory()
    # Clears the entry box
    audio_input.delete(0, tk.END)
    # Inserts the chosen path to the entry box
    audio_input.insert(0, folder_path)

# Checks the validity of the user's inputs
def check_settings(root):
    # Error msg to be shown to the user if sth goes wrong
    error_msg = ''

    # Checks image file path input
    try:
        with Image.open(root.nametowidget("image_frame").nametowidget('image_input').get()) as img:
            img.verify()
    except (IOError, SyntaxError):
        error_msg += 'Invalid image file\n'

    # Checks audio folder path input
    if not os.path.isdir(root.children.get('audio_frame').nametowidget('audio_input').get()):
        error_msg += 'Invalid audio folder\n'

    # Checks save folder path input
    if not os.path.isdir(root.children.get('save_frame').nametowidget('save_input').get()):
        error_msg += 'Invalid save folder\n'


    # Checks the resolution input
    width = root.children.get('vidsets_frame').nametowidget('width_input').get()
    height = root.children.get('vidsets_frame').nametowidget('height_input').get()
    if width == '' and height == '':
        pass
    elif width != '' and height != '' and width.isdigit() and height.isdigit() and int(width) > 0 and int(height) > 0:
        pass
    else:
        error_msg += 'Invalid resolution\n'


    # Checks the fps input
    fps = root.children.get('vidsets_frame').nametowidget('fps_input').get()
    if not (fps != '' and fps.isdigit() and int(fps) > 0):
        error_msg += 'Invalid FPS\n'


    # Checks the audio fade-in input
    fade_in = root.children.get('audiosets_frame').nametowidget('audiofadein_input').get()
    if fade_in == '':
        pass
    elif fade_in.isdigit() and int(fade_in) > 0:
        pass
    else:
        error_msg += 'Invalid fade-in seconds\n'

    # Checks the audio fade-out input
    fade_out = root.children.get('audiosets_frame').nametowidget('audiofadeout_input').get()
    if fade_out == '':
        pass
    elif fade_out.isdigit() and int(fade_out) > 0:
        pass
    else:
        error_msg += 'Invalid fade-out seconds\n'


    # Checks the hours input
    hours = root.children.get('extrasets_frame').nametowidget('hours_input').get()
    if hours == '':
        pass
    elif hours.isdigit() and int(hours) > 0:
        pass
    else:
        error_msg += 'Invalid hours\n'


    # Checks the mins input
    mins = root.children.get('extrasets_frame').nametowidget('mins_input').get()
    if mins == '':
        pass
    elif mins.isdigit() and int(mins) > 0:
        pass
    else:
        error_msg += 'Invalid mins\n'


    # Checks the secs input
    secs = root.children.get('extrasets_frame').nametowidget('secs_input').get()
    if secs == '':
        pass
    elif secs.isdigit() and int(secs) > 0:
        pass
    else:
        error_msg += 'Invalid secs\n'



    # Checks the save file path input
    if not is_valid_filename(root.children.get('export_frame').nametowidget('export_input').get()):
        error_msg += 'Invalid save file name\n'


    # Shows an error message to the user if any input was invalid
    if error_msg != '':
        tk.messagebox.showerror(title='Invalid Settings', message=error_msg)
        return False
    else:
        return True


# Saves the current settings and returns them
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
        'max_hours': root.children.get('extrasets_frame').nametowidget('hours_input').get(),
        'max_mins': root.children.get('extrasets_frame').nametowidget('mins_input').get(),
        'max_secs': root.children.get('extrasets_frame').nametowidget('secs_input').get(),
        'file_name': root.children.get('export_frame').nametowidget('export_input').get()
    }

    # Opens a file and writes the dictionary into it
    with open('settings.json', 'w') as file:
        json.dump(settings_dict, file)

    return settings_dict

# Loads the settings
def load_settings():
    # Tries to open a file to load the settings and return them
    try:
        with open('settings.json', 'r') as file:
            settings_dict = json.load(file)
        return settings_dict
    except FileNotFoundError:
        print("No settings file found.")
        return
    except json.JSONDecodeError:
        print("Error decoding the settings file")
        return


def get_audio_clips(settings):
    # Gets all the audio files from the given folder and ignored the other types of files
    audio_files = []
    for file in os.listdir(settings.get('audio_folder')):
        if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.aac') or file.endswith(
                '.flac') or file.endswith('.m4a') or file.endswith('.m4b') or file.endswith(
                '.wma') or file.endswith('.aiff') or file.endswith('.ogg'):
            audio_files.append(file)
        else:
            print('Invalid file format found')

    # Checks if there was at least one audio file
    if len(audio_files) != 0:
        audio_clips = []
        total_duration = 0
        for audio in audio_files:
            # Creates an AudioFileClip
            audio_clip = AudioFileClip(settings.get('audio_folder') + '/' + audio)
            # Adds the duration
            total_duration += audio_clip.duration

            # Adds fade-in/fade-out effects to the audio
            if settings.get('fade_in_secs').isdigit():
                audio_clip = audio_clip.fx(audio_fadein, int(settings.get('fade_in_secs')))
            if settings.get('fade_out_secs').isdigit():
                audio_clip = audio_clip.fx(audio_fadeout, int(settings.get('fade_out_secs')))

            audio_clips.append(audio_clip)

        # Mixxes all the audio clips together
        mixxed_audio = concatenate_audioclips(audio_clips)

        # Returns the mixxed clips and their total duration
        return mixxed_audio, round(total_duration)
    # Shows an error msg if there were 0 audio files
    else:
        tk.messagebox.showerror(title='Audio files error', message='0 audio files found')
        return None, 0


# Exports the video
def export_video(root):
    # Checks the validity of the given settings
    if check_settings(root):
        # Saves the given settings for the next session
        settings = save_settings(root)

        # Calculates the max duration of each part if given
        max_duration = 0
        if settings.get('max_hours') != '':
            max_duration += int(settings.get('max_hours'))*60*60
        if settings.get('max_mins') != '':
            max_duration += int(settings.get('max_mins'))*60
        if settings.get('max_secs') != '':
            max_duration += int(settings.get('max_secs'))

        # Gets the audio for the video and its duration
        mixxed_audio, total_duration = get_audio_clips(settings)
        if mixxed_audio != None:
            final_clips = []
            try:
                # Creates image clip with the given image
                image_clip = ImageClip(settings.get('image_file'))

                # Mixxes the image clip with the audio
                mixxed_clip = image_clip.set_audio(mixxed_audio).set_duration(total_duration)

                # Cuts the video into seperate parts if a max duration was given
                if max_duration > 0:
                    starting_point = 0
                    while total_duration > max_duration:
                        final_clips.append(mixxed_clip.subclip(starting_point, starting_point + max_duration))
                        starting_point += max_duration - 1
                        total_duration -= max_duration

                    final_clips.append(mixxed_clip.subclip(starting_point, starting_point + total_duration))
                else:
                    final_clips.append(mixxed_clip)

            except ValueError:
                print('Problem with the image path')
                return


            # Exports the final video
            try:
                # If there are seperate parts, a clip number is added to the file name
                if len(final_clips) != 1:
                    clip_number = 1
                    for final_clip in final_clips:
                        save_file_name = settings.get('save_folder') + '/' + settings.get('file_name') + str(clip_number) + '.mp4'
                        final_clip.write_videofile(save_file_name, codec='libx264', audio_bitrate='3000k', fps=int(settings.get('fps')))
                        clip_number += 1
                else:
                    save_file_name = settings.get('save_folder') + '/' + settings.get('file_name') + '.mp4'

                    final_clips[0].write_videofile(save_file_name, codec='libx264', audio_bitrate='3000k', fps=int(settings.get('fps')))

            except ValueError:
                print('Problem with the save path')
                return
        else:
            return False
    else:
        return False

# Creates a frame for the image input area
def create_image_frame(root, settings):
    image_frame = tk.Frame(root, name="image_frame")
    image_frame.pack(pady=10)

    image_label = tk.Label(image_frame, text="Image File")
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

    audio_label = tk.Label(audio_frame, text="Audio Folder")
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

    save_label = tk.Label(save_frame, text="Save Folder")
    save_label.pack(side=tk.TOP, anchor='w')

    save_input = tk.Entry(save_frame, width=50, name="save_input")
    save_input.insert(0, settings.get('save_folder'))
    save_input.pack(side=tk.LEFT, padx=5)

    save_button = tk.Button(save_frame, text="Explore", command=lambda: select_folder(save_input))
    save_button.pack(side=tk.LEFT, padx=5)

# Creates a frame for the video settings area
def create_vidsets_frame(root, settings):
    vidsets_frame = tk.Frame(root, name="vidsets_frame")
    vidsets_frame.pack(pady=10)

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
    audiosets_frame.pack(pady=10)

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

# Creates a frame for the extra settings area
def create_extrasets_frame(root, settings):
    extrasets_frame = tk.Frame(root, name="extrasets_frame")
    extrasets_frame.pack(pady=10)

    extrasets_label = tk.Label(extrasets_frame, text="Extra Settings")
    extrasets_label.pack(side=tk.TOP, anchor='w', pady=10)

    max_dur_label = tk.Label(extrasets_frame, text="Max Duration: ")
    max_dur_label.pack(side=tk.LEFT, anchor='w', padx=3)

    hours_label = tk.Label(extrasets_frame, text="Hrs")
    hours_label.pack(side=tk.LEFT, anchor='w')

    hours_input = tk.Entry(extrasets_frame, width=4, justify="center", name="hours_input")
    hours_input.insert(0, settings.get('max_hours'))
    hours_input.pack(side=tk.LEFT, padx=1)

    mins_label = tk.Label(extrasets_frame, text="Mins")
    mins_label.pack(side=tk.LEFT, anchor='w')

    mins_input = tk.Entry(extrasets_frame, width=4, justify="center", name="mins_input")
    mins_input.insert(0, settings.get('max_mins'))
    mins_input.pack(side=tk.LEFT, padx=1)

    secs_label = tk.Label(extrasets_frame, text="Secs")
    secs_label.pack(side=tk.LEFT, anchor='w')

    secs_input = tk.Entry(extrasets_frame, width=4, justify="center", name="secs_input")
    secs_input.insert(0, settings.get('max_secs'))
    secs_input.pack(side=tk.LEFT, padx=1)

# Creates a frame for the extra settings area
def create_export_frame(root, settings):
    export_frame = tk.Frame(root, name="export_frame")
    export_frame.pack(pady=10)

    export_label = tk.Label(export_frame, text="File Name")
    export_label.pack(side=tk.TOP, anchor='w')

    export_input = tk.Entry(export_frame, width=50, name="export_input")
    export_input.insert(0, settings.get('file_name'))
    export_input.pack(side=tk.LEFT, padx=5)

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



# TODO: Audio normalizing
# TODO: Tooltips
# TODO: Codecs and bitrates
