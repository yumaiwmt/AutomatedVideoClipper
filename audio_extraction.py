import whisper
from moviepy.editor import VideoFileClip
import os

def audio_extraction(video_path, output_audio_path="audio.mp3"):
    video = VideoFileClip(video_path)
    audio = video.audio
    
    audio.write_audiofile(output_audio_path, logger=None)
    
    audio.close()
    video.close()
    return output_audio_path

audio_file = audio_extraction("input_video.mp4")