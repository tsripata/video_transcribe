#!/usr/bin/env python3
"""
Example script demonstrating how to use the video transcriber programmatically.
This shows how to integrate the transcriber into your own Python code.
"""

import os
from pathlib import Path
from video_transcriber import process_video_folder

def example_basic_usage():
    """Example of basic usage."""
    print("Example 1: Basic Usage")
    print("-" * 30)
    
    # Example folder path (modify this to your actual video folder)
    video_folder = "/path/to/your/video/folder"
    output_file = "example_output.csv"
    
    if os.path.exists(video_folder):
        print(f"Processing videos in: {video_folder}")
        print(f"Output will be saved to: {output_file}")
        
        # Process the folder with automatic language detection
        process_video_folder(video_folder, output_file)
        
        print(f"Check {output_file} for results!")
    else:
        print(f"Folder {video_folder} does not exist.")
        print("Please modify the script with a valid path.")

def example_forced_language():
    """Example of forcing specific language transcription."""
    print("\nExample 2: Forced Language Transcription")
    print("-" * 40)
    
    video_folder = "/path/to/your/video/folder"
    output_file = "thai_transcriptions.csv"
    
    if os.path.exists(video_folder):
        print(f"Processing videos in: {video_folder}")
        print(f"Output will be saved to: {output_file}")
        print("Forcing Thai transcription...")
        
        # Process the folder with forced Thai language
        process_video_folder(video_folder, output_file, language="th")
        
        print(f"Check {output_file} for Thai transcriptions!")
    else:
        print(f"Folder {video_folder} does not exist.")
        print("Please modify the script with a valid path.")

def example_model_selection():
    """Example of using different model sizes."""
    print("\nExample 3: Model Size Selection")
    print("-" * 30)
    
    video_folder = "/path/to/your/video/folder"
    
    if os.path.exists(video_folder):
        print(f"Processing videos in: {video_folder}")
        
        # Example 1: Fast processing with tiny model
        print("\nFast processing with tiny model:")
        output_tiny = "fast_transcriptions.csv"
        process_video_folder(video_folder, output_tiny, model_size="tiny")
        print(f"Fast results saved to: {output_tiny}")
        
        # Example 2: High accuracy with large model
        print("\nHigh accuracy with large model:")
        output_large = "accurate_transcriptions.csv"
        process_video_folder(video_folder, output_large, model_size="large")
        print(f"Accurate results saved to: {output_large}")
        
    else:
        print(f"Folder {video_folder} does not exist.")
        print("Please modify the script with a valid path.")

def example_custom_output():
    """Example with custom output file."""
    print("\nExample 4: Custom Output File")
    print("-" * 30)
    
    video_folder = "/path/to/your/video/folder"
    custom_output = "my_custom_transcriptions.csv"
    
    if os.path.exists(video_folder):
        print(f"Processing videos in: {video_folder}")
        print(f"Output will be saved to: {custom_output}")
        
        # Process with custom output filename
        process_video_folder(video_folder, custom_output)
        
        print(f"Check {custom_output} for results!")
    else:
        print(f"Folder {video_folder} does not exist.")
        print("Please modify the script with a valid path.")

def example_batch_processing():
    """Example of processing multiple folders."""
    print("\nExample 5: Batch Processing Multiple Folders")
    print("-" * 30)
    
    # List of folders to process
    video_folders = [
        "/path/to/folder1",
        "/path/to/folder2",
        "/path/to/folder3"
    ]
    
    for i, folder in enumerate(video_folders, 1):
        if os.path.exists(folder):
            output_file = f"batch_output_{i}.csv"
            print(f"Processing folder {i}: {folder}")
            print(f"Output: {output_file}")
            
            # Process each folder
            process_video_folder(folder, output_file)
            print(f"Completed folder {i}\n")
        else:
            print(f"Folder {folder} does not exist, skipping...\n")

def main():
    """Run all examples."""
    print("Video Transcriber - Usage Examples")
    print("=" * 50)
    
    # Note: These examples use placeholder paths
    # Modify the paths to point to your actual video folders
    
    print("Note: These examples use placeholder paths.")
    print("Please modify the script with valid paths before running.\n")
    
    # Uncomment the examples you want to run:
    
    # example_basic_usage()
    # example_forced_language()
    # example_model_selection()
    # example_custom_output()
    # example_batch_processing()
    
    print("To run examples:")
    print("1. Edit this script and replace placeholder paths with real paths")
    print("2. Uncomment the example functions you want to run")
    print("3. Run: python example_usage.py")
    
    print("\nOr use the command line directly:")
    print("python video_transcriber.py /path/to/video/folder")
    print("\nLanguage options:")
    print("  -l th    : Force Thai transcription")
    print("  -l en    : Force English transcription")
    print("  -l auto  : Automatic language detection (default)")
    print("\nModel options:")
    print("  -m tiny  : Fastest, lowest accuracy")
    print("  -m base  : Balanced speed/accuracy (default)")
    print("  -m small : Better accuracy, slower")
    print("  -m medium: High accuracy, slower")
    print("  -m large : Highest accuracy, slowest")

if __name__ == "__main__":
    main()
