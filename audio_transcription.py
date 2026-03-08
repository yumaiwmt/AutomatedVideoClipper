import whisper
import json
import os


def transcribe_audio(audio_path, model_size="base", output_json_path="transcript.json"):
    model = whisper.load_model("large-v3-turbo")

    """
WHISPER MODEL TAXONOMY (FULL LIST)
---------------------------------------------------------------------------------
| Category    | Model Name        | Parameters | VRAM  | Best Use Case          |
|-------------|-------------------|------------|-------|------------------------|
| LIGHTWEIGHT | tiny / tiny.en    | 39M        | ~1GB  | Extreme speed, English |
|             | base / base.en    | 74M        | ~1GB  | Low-resource devices   |
|-------------|-------------------|------------|-------|------------------------|
| BALANCED    | small / small.en  | 244M       | ~2GB  | Quick JP drafts        |
|             | medium / medium.en| 769M       | ~5GB  | Reliable multi-lang    |
|-------------|-------------------|------------|-------|------------------------|
| LEGACY      | large-v1          | 1550M      | ~10GB | Deprecated             |
|             | large-v2          | 1550M      | ~10GB | Robust, but slower     |
|-------------|-------------------|------------|-------|------------------------|
| SOTA (JP)   | large-v3 / large  | 1550M      | ~10GB | Max Accuracy (Kanji)   |
|             | large-v3-turbo    | 809M       | ~6GB  | Best Speed/Accuracy    |
|             | turbo             | 809M       | ~6GB  | Alias for v3-turbo     |
---------------------------------------------------------------------------------
* Note: '.en' models are optimized for English ONLY. 
* 'large' is typically an alias that points to the most recent 'large-vX' version.
"""

    result = model.transcribe(audio_path, language="ja", verbose=False)

    transcript_data = result["segments"]
    
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(transcript_data, f, ensure_ascii=False, indent=4)
    
    return output_json_path


if __name__ == "__main__":
    audio_file = "audio.mp3"
    if os.path.exists(audio_file):
        data = transcribe_audio(audio_file)
        for item in data[:3]:
            print(f"[{item['start']:.2f}s - {item['end']:.2f}s] {item['text']}")
    else:
        print(f"エラー: {audio_file} が見つかりません。先にAgent 1を実行してください。")