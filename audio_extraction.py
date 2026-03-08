from moviepy import VideoFileClip
import os

def audio_extraction(video_path, output_audio_path="audio.mp3"):
    video = VideoFileClip(video_path)
    audio = video.audio.write_audiofile(output_audio_path, fps=16000, logger=None)
    
    video.close()
    return output_audio_path