import os
import string
from moviepy.editor import AudioFileClip
import yt_dlp

def MP4ToMP3(mp4,mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

def download_youtube_video(url, folder_path, media_type, i=None):
    ydl_opts = {
        'outtmpl' : os.path.join(folder_path, '%(title)s.%(ext)s'),
        'format' : 'bestaudio/best' if media_type == 'audio' else 'best',
        'postprocessors': [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality' : '192',

        }] if media_type == 'audio' else []
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url,download = True)
        if media_type == 'audio':
            title = info_dict.get('title','temp_file')
            input_file = os.path.join(folder_path,f"{title}.mp4")
            output_file = os.path.join(folder_path,f"{title}.mp3")
            if os.path.exists(input_file):
                MP4ToMP3(input_file,output_file)
                os.remove(input_file)

def download_from_file(filename, folder_path, media_type):
    with open(filename, "r") as file:
        links = file.readlines()
        for i, link in enumerate(links,start= 1):
            download_youtube_video(link.strip(),folder_path,media_type, i)
    print("Finished")

def download_playlist(playlist_link, foldre_path, media_type):
    ydl_opts = {
        'outtmpl' : os.path.join(folder_path, '%(title)s.%(ext)s'),
        'format' : 'bestaudio/best' if media_type == 'audio' else 'best',
        'postprocessors': [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality' : '192',

        }] if media_type == 'audio' else []
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_dict = ydl.extract_info(playlist_link, download = True)
    
    print("Finished")

# Driver code

folder_path = input("Enter destination folder path : ")
media_type = input("Enter preffered media type(audio or video) : ")

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

type_input = int(input("Enter how do you want to download?\n1.Single video link\n2.Youtube Playlist link\n3.File with youtube links\n"))

if type_input == 1:
    link = input("Enter video link : ")
    download_youtube_video(link,folder_path,media_type)
elif type_input == 2:
    playlist_link = input("Enter playlist link : ")
    download_playlist(playlist_link,folder_path,media_type)
elif type_input == 3:
    filename = input("Enter file location : ")
    if not os.path.exists(filename):
        print("File not found, Check and try again\nExiting")
        exit(0)
    download_from_file(filename,folder_path,media_type)
else:
    print("Something went wrong ! \nExiting")
    exit(0)

# Complete
