import os
from audio_extraction import audio_extraction
from audio_transcription import transcribe_audio

def run_pipeline(video_filename):
    print("Starting Automated Video Clipper Pipeline")
    
    base_name = os.path.splitext(video_filename)[0] 
    audio_output = f"{base_name}_audio.mp3"
    json_output = f"{base_name}_transcript.json"

    if not os.path.exists(video_filename):
        print(f"Video file not found.")
        return

# Phase 1: Audio Extraction

    print(f"Starting audio extraction from {video_filename}")
    audio_path = audio_extraction(video_filename, audio_output)
    print(f"Audio saved as: {audio_path}")

# Phase 2: Audio Transcription (OpenAI Whisper)

    print(f"Transcribing {audio_path}")
    try:
        json_path = transcribe_audio(audio_path, output_json_path=json_output)
        print(f"Transcription saved as: {json_path}")
    except Exception as e:
        print(f"Transcription failed: {e}")
        return
    
# Phase 3: OCR Overlay

    print("Starting OCR overlay extraction")
    try:
        overlay_json_path = extract_overlay(video_filename, sample_rate=1.0, lang="jpn", output_json_path=f"{base_name}_overlay.json")
        print(f"OCR overlay extraction completed. Results saved to {overlay_json_path}")
    except Exception as e:
        print(f"OCR overlay extraction failed: {e}")
        return

    print("\nPipeline Completed.")

if __name__ == "__main__":
    video = "short_test_vid2.mp4" 
    run_pipeline(video)