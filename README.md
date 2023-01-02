# Pitgamers_ytdl
Pitgamers_ytdl is a Python module that allows you to download YouTube videos and audio with a single line of code. It uses the ytdl.tiodevhost.my.id service to fetch the highest quality video or audio from a given URL.

## Installation
To install the Pitgamers_ytdl module, follow these steps:

Make sure you have the latest version of pip installed: ```bash 
pip install --upgrade pip 
```
Use pip to install the Pitgamers_ytdl module: ```bash
pip install Pitgamers_ytdl
```
Usage
To use the Pitgamers_ytdl module to download videos or audio, you can do the following:

Copy code
import Pitgamers_ytdl

# Replace "video_url" with the URL of the video you want to download
Pitgamers_ytdl.download_video(video_url)

# Replace "audio_url" with the URL of the audio you want to download
Pitgamers_ytdl.download_audio(audio_url)
The downloaded file will be saved in the current working directory. If you want to save it to a different location, you can specify the file path when opening the file for writing:

Copy code
with open("/path/to/save/file/file_name.mp4", "wb") as f:
  f.write(response.content)
Replace "file_name.mp4" with the desired file name and make sure to specify the correct file extension (".mp4" for video and ".mp3" for audio).

License
The Pitgamers_ytdl module is licensed under the MIT License. See the LICENSE file for more details.
