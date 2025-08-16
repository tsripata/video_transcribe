#!/usr/bin/env python3
"""
Demonstration script showing all available options for the video transcriber.
This script demonstrates the various combinations of language, model, and output options.
"""

import os
import sys
from pathlib import Path

# Add the current directory to Python path to import video_transcriber
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from video_transcriber import process_video_folder
except ImportError:
    print("Error: Could not import video_transcriber module")
    print("Make sure video_transcriber.py is in the same directory")
    sys.exit(1)

def demo_all_options():
    """Demonstrate all available options."""
    print("Video Transcriber - All Options Demo")
    print("=" * 50)
    
    # Example folder path (modify this to your actual video folder)
    video_folder = "/path/to/your/video/folder"
    
    if not os.path.exists(video_folder):
        print(f"Video folder {video_folder} does not exist.")
        print("Please modify the script with a valid path.")
        return
    
    print(f"Video folder: {video_folder}")
    print()
    
    # Demo 1: Basic usage (auto language, base model)
    print("Demo 1: Basic Usage (Auto Language, Base Model)")
    print("-" * 50)
    output_basic = "demo_basic.csv"
    try:
        process_video_folder(video_folder, output_basic)
        print(f"✓ Basic transcription completed: {output_basic}")
    except Exception as e:
        print(f"✗ Basic transcription failed: {e}")
    print()
    
    # Demo 2: Force Thai with small model
    print("Demo 2: Force Thai Language, Small Model")
    print("-" * 45)
    output_thai_small = "demo_thai_small.csv"
    try:
        process_video_folder(video_folder, output_thai_small, language="th", model_size="small")
        print(f"✓ Thai transcription with small model completed: {output_thai_small}")
    except Exception as e:
        print(f"✗ Thai transcription with small model failed: {e}")
    print()
    
    # Demo 3: Force English with large model
    print("Demo 3: Force English Language, Large Model")
    print("-" * 47)
    output_english_large = "demo_english_large.csv"
    try:
        process_video_folder(video_folder, output_english_large, language="en", model_size="large")
        print(f"✓ English transcription with large model completed: {output_english_large}")
    except Exception as e:
        print(f"✗ English transcription with large model failed: {e}")
    print()
    
    # Demo 4: Auto language with tiny model (fastest)
    print("Demo 4: Auto Language, Tiny Model (Fastest)")
    print("-" * 45)
    output_auto_tiny = "demo_auto_tiny.csv"
    try:
        process_video_folder(video_folder, output_auto_tiny, model_size="tiny")
        print(f"✓ Auto language with tiny model completed: {output_auto_tiny}")
    except Exception as e:
        print(f"✗ Auto language with tiny model failed: {e}")
    print()
    
    # Demo 5: Auto language with medium model (balanced)
    print("Demo 5: Auto Language, Medium Model (Balanced)")
    print("-" * 47)
    output_auto_medium = "demo_auto_medium.csv"
    try:
        process_video_folder(video_folder, output_auto_medium, model_size="medium")
        print(f"✓ Auto language with medium model completed: {output_auto_medium}")
    except Exception as e:
        print(f"✗ Auto language with medium model failed: {e}")
    print()
    
    print("=" * 50)
    print("All demos completed!")
    print("\nGenerated files:")
    demo_files = [
        output_basic, output_thai_small, output_english_large, 
        output_auto_tiny, output_auto_medium
    ]
    for file in demo_files:
        if os.path.exists(file):
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} (not created)")

def show_command_line_equivalents():
    """Show the command line equivalents for the demos."""
    print("\n" + "=" * 50)
    print("Command Line Equivalents")
    print("=" * 50)
    
    print("The demos above are equivalent to these command line calls:")
    print()
    
    print("Demo 1: Basic Usage")
    print("python video_transcriber.py /path/to/videos")
    print()
    
    print("Demo 2: Force Thai, Small Model")
    print("python video_transcriber.py /path/to/videos -l th -m small")
    print()
    
    print("Demo 3: Force English, Large Model")
    print("python video_transcriber.py /path/to/videos -l en -m large")
    print()
    
    print("Demo 4: Auto Language, Tiny Model")
    print("python video_transcriber.py /path/to/videos -m tiny")
    print()
    
    print("Demo 5: Auto Language, Medium Model")
    print("python video_transcriber.py /path/to/videos -m medium")
    print()
    
    print("All Options Summary:")
    print("  -l, --language: th, en, auto (default: auto)")
    print("  -m, --model: tiny, base, small, medium, large (default: base)")
    print("  -o, --output: output filename (default: transcription_output.csv)")

def main():
    """Main function."""
    print("Video Transcriber - Complete Options Demonstration")
    print("=" * 60)
    
    print("This script demonstrates all available options:")
    print("• Language forcing (Thai, English, or Auto)")
    print("• Model size selection (tiny to large)")
    print("• Output file customization")
    print()
    
    print("Note: You need to modify the video_folder path in the script")
    print("to point to a folder containing your video files.")
    print()
    
    # Check if video folder path needs to be updated
    video_folder = "/path/to/your/video/folder"
    if video_folder == "/path/to/your/video/folder":
        print("⚠️  Please update the video_folder path in this script first!")
        print("   Edit line 25 to point to your actual video folder.")
        return
    
    # Run the demos
    demo_all_options()
    show_command_line_equivalents()

if __name__ == "__main__":
    main()
