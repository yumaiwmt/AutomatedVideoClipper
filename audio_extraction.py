from moviepy import VideoFileClip
import os

def audio_extraction(video_path, output_audio_path="audio.mp3"):
    video = VideoFileClip(video_path)
    audio = video.audio.write_audiofile(output_audio_path, fps=16000, logger=None)
    
    video.close()
    return output_audio_path

if __name__ == "__main__":
    input_video = "short_test_vid.mp4"
    if os.path.exists(input_video):
        audio_file = audio_extraction(input_video)
        print(f"抽出完了: {audio_file}")
    else:
        print(f"エラー: {input_video} が見つかりません。")