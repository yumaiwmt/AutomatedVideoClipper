import whisper
import json
import os


def transcribe_audio(audio_path, model_size="base", output_json_path="transcript.json"):
    model = whisper.load_model("turbo")

    """
WHISPER MODEL COMPARISON (FOR JAPANESE TRANSCRIPTION)
---------------------------------------------------------------------------
| Model Size | Parameters | VRAM Needed | Speed    | Best Use Case        |
|------------|------------|-------------|----------|----------------------|
| Tiny       | 39M        | ~1 GB       | ~10x-32x | Super fast drafts.   |
| Base       | 74M        | ~1 GB       | ~7x-16x  | Mobile/low-power.    |
| Small      | 244M       | ~2 GB       | ~4x      | Clean audio balance. |
| Medium     | 769M       | ~5 GB       | ~2x      | Non-English general. |
| Large-v3   | 1550M      | ~10 GB      | 1x       | GOLD STANDARD (JA).  |
| Turbo      | 809M       | ~6 GB       | ~6x-8x   | TOP CHOICE (Speed).  |
---------------------------------------------------------------------------
Note: VRAM requirements may vary based on implementation (e.g., faster-whisper).
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