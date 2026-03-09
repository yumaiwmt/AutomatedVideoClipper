# Automated Video Clipper Project

## 📋 Overview

The **Automated Video Clipper** is a Python-based pipeline that intelligently processes video files by:
- Extracting audio from video files
- Transcribing audio using OpenAI's Whisper ASR (Automatic Speech Recognition)
- Extracting on-screen text (overlay/subtitles) using OCR (Optical Character Recognition)

This tool is designed to automatically generate transcriptions and text overlays from video content, making it easy to create clip-ready metadata for video editing and analysis workflows.

## ✨ Features

- **Audio Extraction**: Automatically extract audio from video files (supports multiple formats)
- **Audio Transcription**: Uses OpenAI Whisper for accurate speech-to-text conversion with support for multiple languages
- **OCR Overlay Detection**: Extracts on-screen text from video frames with timestamp tracking
- **JSON Output**: All results are exported as structured JSON for easy integration with other tools
- **Configurable Parameters**: Adjust transcription model size, OCR language, and sampling rates

## 📦 Requirements

Before installing dependencies, ensure you have the following:

- **Python 3.8 or higher**
- **FFmpeg**: Required for audio/video processing
  - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) or use `choco install ffmpeg`
  - **macOS**: `brew install ffmpeg`
  - **Linux**: `sudo apt-get install ffmpeg`
- **Tesseract OCR**: Required for text extraction
  - **Windows**: Download installer from [GitHub tesseract releases](https://github.com/UB-Mannheim/tesseract/wiki) and run the installation
  - **macOS**: `brew install tesseract`
  - **Linux**: `sudo apt-get install tesseract-ocr`

## 🚀 Installation

### Step 1: Clone or Download the Repository

```bash
cd AutomatedVideoClipperProject
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Or manually install the required packages:**

```bash
pip install moviepy
pip install openai-whisper
pip install opencv-python
pip install pytesseract
pip install Pillow
```

### Step 4: Install System Dependencies

#### Windows Users:
1. **FFmpeg**: Download and install from [ffmpeg.org](https://ffmpeg.org/download.html), or use package manager:
   ```bash
   choco install ffmpeg
   ```

2. **Tesseract OCR**: Download the Windows installer from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki) and run it.
   - Default installation path: `C:\Program Files\Tesseract-OCR`
   - You may need to configure the path in your code if installed elsewhere

#### macOS Users:
```bash
brew install ffmpeg tesseract
```

#### Linux Users:
```bash
sudo apt-get install ffmpeg tesseract-ocr
```

## 📖 Usage

### Basic Usage

1. **Prepare Your Video File**: Place your video file in the project directory (or specify the path in the code)

2. **Run the Pipeline**:
   ```bash
   python main.py
   ```

   By default, the script looks for `short_test_vid2.mp4`. Modify the `main.py` file to use your own video:
   ```python
   if __name__ == "__main__":
       video = "your_video_file.mp4"  # Change this to your video file
       run_pipeline(video)
   ```

3. **Output Files**: The pipeline generates three output files:
   - `{video_name}_audio.mp3` - Extracted audio
   - `{video_name}_transcript.json` - Transcription with timestamps
   - `{video_name}_overlay.json` - OCR text overlays with timestamps

### Output Format

**Transcript JSON** (`{video}_transcript.json`):
```json
{
  "text": "Full transcribed text...",
  "segments": [
    {
      "id": 0,
      "seek": 0,
      "start": 0.0,
      "end": 2.5,
      "text": "Transcribed segment text",
      "tokens": [...]
    }
  ]
}
```

**Overlay JSON** (`{video}_overlay.json`):
```json
[
  {
    "start_time": 1.5,
    "end_time": 5.2,
    "text": "On-screen text detected"
  }
]
```

## 🏗️ Project Structure

```
AutomatedVideoClipperProject/
├── main.py                          # Main pipeline orchestrator
├── audio_extraction.py              # Audio extraction module  
├── audio_transcription.py           # Whisper transcription module
├── overlay_text_extraction.py       # OCR extraction module
├── cpu_testing.py                   # Performance testing utilities
├── short_test_vid2_transcript.json  # Sample output
├── README.md                        # This file
└── __pycache__/                     # Python cache directory
```

## 🔧 Configuration Options

### Audio Transcription Models

The Whisper model can be adjusted in `audio_transcription.py`:

| Model | Parameters | VRAM | Best Use |
|-------|-----------|------|----------|
| `tiny` | 39M | ~1GB | Maximum speed, English only |
| `base` | 74M | ~1GB | Low-resource devices |
| `small` | 244M | ~2GB | Fast Japanese transcription |
| `medium` | 769M | ~5GB | Reliable multi-language |
| `large-v3` | 1550M | ~10GB | Highest accuracy (Kanji support) |
| `large-v3-turbo` | 809M | ~6GB | **Best balanced choice** |

### OCR Configuration

In `overlay_text_extraction.py`, adjust these parameters:

```python
extract_overlay(
    video_filename,
    sample_rate=1.0,      # Frame sampling (e.g., 0.5 = every other frame)
    lang="jpn",           # Tesseract language code
    output_json_path="..." # Output file path
)
```

**Supported Languages**:
- `jpn` - Japanese
- `eng` - English
- `fra` - French
- `deu` - German
- `chi_sim` - Simplified Chinese
- See [Tesseract docs](https://github.com/UB-Mannheim/tesseract/wiki) for full list

## 🤔 Troubleshooting

### "Tesseract not found" error
- **Windows**: Ensure Tesseract is installed and add this to your code:
  ```python
  import pytesseract
  pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```

### "FFmpeg not found" error
- Ensure FFmpeg is properly installed and in your system PATH
- Test with: `ffmpeg -version`

### "Whisper model download fails"
- Check your internet connection
- Models are downloaded to `~/.cache/whisper/`
- You can pre-download models using: `whisper --model large-v3-turbo --help`

### Audio extraction is slow
- Use `moviepy` with ffmpeg-python backend for better performance
- Reduce audio quality/sample rate if not needed

## 📚 Dependencies Summary

| Package | Purpose | Version |
|---------|---------|---------|
| moviepy | Video/audio processing | Latest |
| openai-whisper | Speech-to-text transcription | Latest |
| opencv-python | Video frame processing | Latest |
| pytesseract | OCR text extraction | Latest |
| Pillow | Image processing | Latest |

## 📝 License

This project is provided as-is for personal and educational use.

## 🤝 Contributing

Feel free to submit issues or improvements!

## 📧 Support

For issues or questions, please check the troubleshooting section or review the code comments for additional guidance.

---

**Last Updated**: March 2026
