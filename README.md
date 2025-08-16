# Video Transcriber

A Python script that transcribes video files (MOV/MP4) using OpenAI's WhisperAI and outputs the results to a CSV file. The script automatically detects and transcribes both Thai and English audio.

## Features

- Supports MOV and MP4 video formats
- Automatic language detection (Thai/English)
- Extracts audio using ffmpeg
- Generates timestamped transcriptions
- Outputs results in CSV format with columns:
  - File Name
  - Time (minutes)
  - Transcribed Text
- Handles multiple video files in a folder
- Temporary audio file cleanup

## Prerequisites

### 1. Install ffmpeg

The script requires ffmpeg for audio extraction and video duration detection.

**macOS (using Homebrew):**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python video_transcriber.py /path/to/video/folder
```

### Specify Output File

```bash
python video_transcriber.py /path/to/video/folder -o my_transcriptions.csv
```

### Force Thai Transcription

```bash
python video_transcriber.py /path/to/video/folder -l th
```

### Force English Transcription

```bash
python video_transcriber.py /path/to/video/folder -l en
```

### Combine Options

```bash
python video_transcriber.py /path/to/video/folder -l th -o thai_transcriptions.csv
```

### Use Different Model Sizes

```bash
# Fast transcription with tiny model
python video_transcriber.py /path/to/video/folder -m tiny

# High accuracy with large model
python video_transcriber.py /path/to/video/folder -m large

# Combine language and model options
python video_transcriber.py /path/to/video/folder -l th -m medium -o thai_accurate.csv
```

### Command Line Arguments

- `folder`: Path to the folder containing video files (required)
- `-o, --output`: Output CSV file path (optional, defaults to `transcription_output.csv`)
- `-l, --language`: Force transcription language (optional, defaults to auto-detection)
  - `th`: Force Thai transcription
  - `en`: Force English transcription
  - `auto`: Automatic language detection (default)
- `-m, --model`: Whisper model size (optional, defaults to "base")
  - `tiny`: Fastest, lowest accuracy
  - `base`: Good balance of speed and accuracy (default)
  - `small`: Better accuracy, slower
  - `medium`: High accuracy, slower
  - `large`: Highest accuracy, slowest

## Example Output

The script generates a CSV file with the following format:

```csv
File Name,Time (mins),Transcribed Text
video1.mp4,0.00,Hello, this is the beginning of the video.
video1.mp4,0.50,Welcome to our presentation today.
video1.mp4,1.20,We will be discussing important topics.
video2.mov,0.00,สวัสดีครับ นี่คือวิดีโอภาษาไทย
video2.mov,0.45,เราจะพูดคุยเกี่ยวกับหัวข้อต่างๆ
```

## How It Works

1. **Video Discovery**: Scans the specified folder for MOV and MP4 files
2. **Audio Extraction**: Uses ffmpeg to extract audio from each video file
3. **Transcription**: Processes audio through WhisperAI with automatic language detection
4. **CSV Generation**: Outputs timestamped transcriptions to CSV format
5. **Cleanup**: Removes temporary audio files

## Model Options

The script uses the "base" Whisper model by default, but you can now specify different models via command line:

- `"tiny"`: Fastest, lowest accuracy (~39 MB, ~1x speed)
- `"base"`: Good balance of speed and accuracy (~74 MB, ~1x speed, default)
- `"small"`: Better accuracy, slower (~244 MB, ~2x speed)
- `"medium"`: High accuracy, slower (~769 MB, ~4x speed)
- `"large"`: Highest accuracy, slowest (~1550 MB, ~8x speed)

### Command Line Usage

```bash
# Use tiny model for fast processing
python video_transcriber.py /path/to/videos -m tiny

# Use large model for maximum accuracy
python video_transcriber.py /path/to/videos -m large

# Combine with language forcing
python video_transcriber.py /path/to/videos -l th -m medium
```

### Model Selection Guidelines

- **`tiny`**: Use for quick previews or when speed is critical
- **`base`**: Good for most use cases, balanced performance
- **`small`**: Better accuracy for important content
- **`medium`**: High accuracy for professional use
- **`large`**: Maximum accuracy for critical transcriptions

## Troubleshooting

### Common Issues

1. **ffmpeg not found**: Install ffmpeg and ensure it's in your system PATH
2. **CUDA/GPU issues**: The script will automatically use CPU if CUDA is not available
3. **Memory issues**: For large videos, consider using a smaller Whisper model
4. **Audio extraction fails**: Ensure the video file is not corrupted and has valid audio

### Performance Tips

- Use SSD storage for faster file I/O
- Close other applications to free up memory
- For batch processing, consider processing videos sequentially to avoid memory issues

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests! 
