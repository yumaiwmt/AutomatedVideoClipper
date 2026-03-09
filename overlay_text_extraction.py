import pytesseract
import cv2
import json
import os

def extract_overlay(video_path, sample_rate = 1.0, lang="jpn", output_json_path="overlay_text.json"):
    if not os.path.exists(video_path):
        print(f"Video file not found: {video_path}")
        return None
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return None
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * sample_rate)

    results = []
    frame_count = 0

    print(f'Extracting text from video frames')

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % frame_interval == 0:
            timestamp = round(frame_count / fps, 2)
            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(grayscale, lang=lang).strip()
            if text:
                if current_entry and current_entry["text"] == text:
                    current_entry["end_time"] = timestamp
                else:
                    if current_entry:
                        results.append(current_entry)
                    current_entry = {
                        "start_time": timestamp,
                        "end_time": timestamp,
                        "text": text
                    }
            else:
                if current_entry:
                    results.append(current_entry)
                    current_entry = None
        frame_count += 1
        
    if current_entry:
        results.append(current_entry)
    
    cap.release()

    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print(f"Overlay text extraction completed. Results saved to {output_json_path}")
    return output_json_path


    