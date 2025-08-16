#!/usr/bin/env python3
"""
Video Transcriber Script
Transcribes video files (MOV/MP4) using WhisperAI and outputs to CSV format.
Supports both Thai and English audio.
"""

import os
import sys
import argparse
import csv
import subprocess
import tempfile
from pathlib import Path
from typing import List, Tuple
import whisper
import torch


def extract_audio_from_video(video_path: str, output_dir: str) -> str:
    """
    Extract audio from video file using ffmpeg.
    
    Args:
        video_path: Path to the video file
        output_dir: Directory to save the extracted audio
        
    Returns:
        Path to the extracted audio file
    """
    video_name = Path(video_path).stem
    audio_path = os.path.join(output_dir, f"{video_name}.wav")
    
    # Use ffmpeg to extract audio
    cmd = [
        "ffmpeg", "-i", video_path,
        "-vn",  # No video
        "-acodec", "pcm_s16le",  # PCM 16-bit
        "-ar", "16000",  # 16kHz sample rate
        "-ac", "1",  # Mono
        "-y",  # Overwrite output file
        audio_path
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        return audio_path
    except subprocess.CalledProcessError as e:
        print(f"Error extracting audio from {video_path}: {e}")
        return None


def get_video_duration(video_path: str) -> float:
    """
    Get video duration in seconds using ffprobe.
    
    Args:
        video_path: Path to the video file
        
    Returns:
        Duration in seconds
    """
    cmd = [
        "ffprobe", "-v", "quiet",
        "-show_entries", "format=duration",
        "-of", "csv=p=0",
        video_path
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        duration = float(result.stdout.strip())
        return duration
    except (subprocess.CalledProcessError, ValueError) as e:
        print(f"Error getting duration for {video_path}: {e}")
        return 0.0


def transcribe_audio(audio_path: str, model, language: str = None) -> List[Tuple[float, float, str]]:
    """
    Transcribe audio using WhisperAI.
    
    Args:
        audio_path: Path to the audio file
        model: Loaded Whisper model
        language: Force language detection ("th" for Thai, "en" for English, None for auto)
        
    Returns:
        List of tuples: (start_time, end_time, text)
    """
    try:
        # Transcribe with timestamps and optional language forcing
        transcribe_options = {"word_timestamps": True}
        if language:
            transcribe_options["language"] = language
            print(f"  Forcing transcription in {language.upper()}")
        
        result = model.transcribe(audio_path, **transcribe_options)
        
        segments = []
        for segment in result["segments"]:
            start_time = segment["start"]
            end_time = segment["end"]
            text = segment["text"].strip()
            
            if text:  # Only add non-empty segments
                segments.append((start_time, end_time, text))
        
        return segments
    except Exception as e:
        print(f"Error transcribing {audio_path}: {e}")
        return []


def seconds_to_minutes(seconds: float) -> float:
    """Convert seconds to minutes."""
    return seconds / 60.0


def process_video_folder(folder_path: str, output_csv: str, language: str = None, model_size: str = "base"):
    """
    Process all video files in the specified folder.
    
    Args:
        folder_path: Path to folder containing video files
        output_csv: Path to output CSV file
        language: Force language detection ("th" for Thai, "en" for English, None for auto)
        model_size: Whisper model size ("tiny", "base", "small", "medium", "large")
    """
    # Check if folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory")
        sys.exit(1)
    
    # Supported video extensions
    video_extensions = {'.mov', '.mp4', '.MOV', '.MP4'}
    
    # Find all video files
    video_files = []
    for file in os.listdir(folder_path):
        if Path(file).suffix in video_extensions:
            video_files.append(os.path.join(folder_path, file))
    
    if not video_files:
        print(f"No video files found in {folder_path}")
        return
    
    print(f"Found {len(video_files)} video files to process")
    
    # Load Whisper model (will download if not present)
    print(f"Loading Whisper model: {model_size}")
    model = whisper.load_model(model_size)
    
    # Create temporary directory for audio files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Prepare CSV output
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['File Name', 'Time (mins)', 'Transcribed Text'])
            
            # Process each video file
            for i, video_path in enumerate(video_files, 1):
                video_name = Path(video_path).name
                print(f"Processing {i}/{len(video_files)}: {video_name}")
                
                # Get video duration
                duration = get_video_duration(video_path)
                if duration == 0:
                    print(f"Skipping {video_name} - could not determine duration")
                    continue
                
                # Extract audio
                audio_path = extract_audio_from_video(video_path, temp_dir)
                if not audio_path:
                    print(f"Skipping {video_name} - could not extract audio")
                    continue
                
                # Transcribe audio
                segments = transcribe_audio(audio_path, model, language)
                
                if segments:
                    # Write segments to CSV
                    for start_time, end_time, text in segments:
                        # Use start time for the timestamp
                        time_mins = seconds_to_minutes(start_time)
                        writer.writerow([video_name, f"{time_mins:.2f}", text])
                    
                    print(f"  Transcribed {len(segments)} segments")
                else:
                    print(f"  No transcription generated for {video_name}")
                
                # Clean up audio file
                if os.path.exists(audio_path):
                    os.remove(audio_path)
    
    print(f"\nTranscription complete! Results saved to {output_csv}")


def main():
    """Main function to handle command line arguments and run the transcriber."""
    parser = argparse.ArgumentParser(
        description="Transcribe video files using WhisperAI and output to CSV"
    )
    parser.add_argument(
        "folder",
        help="Path to folder containing video files (MOV/MP4)"
    )
    parser.add_argument(
        "-o", "--output",
        default="transcription_output.csv",
        help="Output CSV file path (default: transcription_output.csv)"
    )
    parser.add_argument(
        "-l", "--language",
        choices=["th", "en", "auto"],
        default="auto",
        help="Force transcription language: 'th' for Thai, 'en' for English, 'auto' for automatic detection (default: auto)"
    )
    parser.add_argument(
        "-m", "--model",
        choices=["tiny", "base", "small", "medium", "large"],
        default="base",
        help="Whisper model size: 'tiny' (fastest), 'base', 'small', 'medium', 'large' (most accurate) (default: base)"
    )
    
    args = parser.parse_args()
    
    # Convert language choice to actual language code for Whisper
    language_code = None
    if args.language == "th":
        language_code = "th"
    elif args.language == "en":
        language_code = "en"
    # "auto" keeps language_code as None for automatic detection
    
    # Check if ffmpeg is available
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: ffmpeg is not installed or not in PATH")
        print("Please install ffmpeg: https://ffmpeg.org/download.html")
        sys.exit(1)
    
    # Check if ffprobe is available
    try:
        subprocess.run(["ffprobe", "-version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: ffprobe is not installed or not in PATH")
        print("Please install ffmpeg (includes ffprobe): https://ffmpeg.org/download.html")
        sys.exit(1)
    
    # Process the video folder
    process_video_folder(args.folder, args.output, language_code, args.model)


if __name__ == "__main__":
    main()
