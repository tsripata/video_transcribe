#!/usr/bin/env python3
"""
Test script to demonstrate the language forcing functionality.
This script shows how to use the video transcriber with different language options.
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

def test_language_options():
    """Test different language options."""
    print("Testing Language Options for Video Transcriber")
    print("=" * 50)
    
    # Test folder path (modify this to your actual video folder)
    test_folder = "/path/to/your/video/folder"
    
    if not os.path.exists(test_folder):
        print(f"Test folder {test_folder} does not exist.")
        print("Please modify the script with a valid path.")
        return
    
    print(f"Test folder: {test_folder}")
    print()
    
    # Test 1: Automatic language detection
    print("Test 1: Automatic Language Detection")
    print("-" * 35)
    output_auto = "test_auto_detection.csv"
    try:
        process_video_folder(test_folder, output_auto)
        print(f"✓ Automatic detection completed: {output_auto}")
    except Exception as e:
        print(f"✗ Automatic detection failed: {e}")
    print()
    
    # Test 2: Force Thai transcription
    print("Test 2: Force Thai Transcription")
    print("-" * 30)
    output_thai = "test_thai_forced.csv"
    try:
        process_video_folder(test_folder, output_thai, language="th")
        print(f"✓ Thai transcription completed: {output_thai}")
    except Exception as e:
        print(f"✗ Thai transcription failed: {e}")
    print()
    
    # Test 3: Force English transcription
    print("Test 3: Force English Transcription")
    print("-" * 32)
    output_english = "test_english_forced.csv"
    try:
        process_video_folder(test_folder, output_english, language="en")
        print(f"✓ English transcription completed: {output_english}")
    except Exception as e:
        print(f"✗ English transcription failed: {e}")
    print()
    
    print("=" * 50)
    print("Language testing completed!")
    print("\nGenerated files:")
    for file in [output_auto, output_thai, output_english]:
        if os.path.exists(file):
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} (not created)")

def test_model_sizes():
    """Test different model sizes."""
    print("\nTesting Model Sizes for Video Transcriber")
    print("=" * 50)
    
    # Test folder path (modify this to your actual video folder)
    test_folder = "/path/to/your/video/folder"
    
    if not os.path.exists(test_folder):
        print(f"Test folder {test_folder} does not exist.")
        print("Please modify the script with a valid path.")
        return
    
    print(f"Test folder: {test_folder}")
    print()
    
    # Test different model sizes
    models_to_test = [
        ("tiny", "test_tiny_model.csv"),
        ("base", "test_base_model.csv"),
        ("small", "test_small_model.csv")
    ]
    
    for model_name, output_file in models_to_test:
        print(f"Test: {model_name.upper()} Model")
        print("-" * (len(model_name) + 10))
        try:
            process_video_folder(test_folder, output_file, model_size=model_name)
            print(f"✓ {model_name} model completed: {output_file}")
        except Exception as e:
            print(f"✗ {model_name} model failed: {e}")
        print()
    
    print("=" * 50)
    print("Model size testing completed!")
    print("\nGenerated files:")
    for _, output_file in models_to_test:
        if os.path.exists(output_file):
            print(f"  ✓ {output_file}")
        else:
            print(f"  ✗ {output_file} (not created)")

def main():
    """Main function."""
    print("Language Options Test for Video Transcriber")
    print("=" * 50)
    
    print("This script tests language modes and model sizes:")
    print("1. Automatic detection (default)")
    print("2. Force Thai transcription")
    print("3. Force English transcription")
    print("4. Different model sizes (tiny, base, small)")
    print()
    
    print("Note: You need to modify the test_folder path in the script")
    print("to point to a folder containing your video files.")
    print()
    
    # Check if test folder path needs to be updated
    test_folder = "/path/to/your/video/folder"
    if test_folder == "/path/to/your/video/folder":
        print("⚠️  Please update the test_folder path in this script first!")
        print("   Edit line 25 to point to your actual video folder.")
        return
    
    # Run the tests
    test_language_options()
    test_model_sizes()

if __name__ == "__main__":
    main()
