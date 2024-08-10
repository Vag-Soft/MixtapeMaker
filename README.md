# MixtapeMaker

 ![image](https://github.com/user-attachments/assets/e4e71e59-3db0-4183-9d50-43cbfa4124b7)

MixtapeMaker is a simple Python application that allows you to create video mixtapes by combining images and audio files. 
The application has a GUI where users can specify various settings, such as video resolution, frames per second (FPS), audio fade-in/out duration, and more. 
The final output is a video file that includes the selected image and audio files.

## Features
- **Image Selection**
- **Audio Selection**
- **Save Folder Selection**
- **Custom Save File Name**
- **Custom Resolution**
- **Custom FPS**
- **Audio fade-in**
- **Audio fade-out**
- **Audio bitrate**
- **Max Clip Duration**
- **Tooltips**
- **Input checking**

## How to run

### Executable
Download and extract the latest release, then run the executable.

(Windows may prompt a warning saying the app may be dangerous, click "Run anyway" to continue)

### IDE or CLI
Clone this repository, install the following requirements and run.

(I'm suggesting you install the requirements in a virtual environment)

###  Requirements
- Python 3.x
- The following Python packages:
  - moviepy - for video editing
  - pathvalidate - for path validation
  - Pillow - for image modification (version 9.5.0 or lower)
  - tkinter - for GUI creation (comes with Python's standard library)
    
You can install the required packages by running the following pip command:

`pip install -r requirements.txt`

## How to use
- **Image File**: Select an image to be displayed in the video
- **Audio Folder**: Select a folder containing the audio files you want to include
  - (The folder must contain at least one audio file
  - Supported formats: .mp3, .wav, .aac, .flac, .m4a, .m4b, .wma, .aiff, .ogg
  - The other type of files will be ignored
- **Save Folder**: Specify the folder where the final video will be saved
- **Width and Height**: If you want to resize the selected image, set the resolution you want in pixels
  - Both must be empty or both must contain a positive integer
  - The initial image will be stretched or squished, depending on the image and the resolution you set
- **FPS**: Set the FPS you want the video to have
   - Must be a positive integer, can't be empty
- **Fade-in/out**: Specify the duration of fade-in/out effect for each of the audio files
  - Leave empty or 0 for no effect, or type in a positive integer that indicates the duration in seconds
- **Bitrate**: Choose the audio's bitrate. Higher values means better audio quality
- **Max Duration**: Set a max duration so that the final video is cut into seperate videos of that duration
  - Leave empty or 0 for no max duration, or type in a positive integer
- **File Name**: Provide a name for the exported video to be called
  - If there are multiple videos due to the max duration, a clip number will be added at the end of the name
  - WARNING! If there is another video with the same name in the save folder, it will be REPLACED

## Contributing
Feel free to submit issues or pull requests for any bugs or feature requests.

## Attributions
- [moviepy](https://github.com/Zulko/moviepy)
- [pathvalidate](https://github.com/thombashi/pathvalidate)
- [Pillow](https://github.com/python-pillow/Pillow)
- [App Icon](https://www.flaticon.com/free-icon/cassette-tape_10885168?term=mixtape&page=1&position=3&origin=tag&related_id=10885168)

