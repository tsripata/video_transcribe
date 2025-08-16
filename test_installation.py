#!/usr/bin/env python3
"""
Test script to verify that all dependencies are properly installed.
Run this script to check if your environment is ready for video transcription.
"""

import sys
import subprocess

def test_python_version():
    """Test if Python version is compatible."""
    print("✓ Python version:", sys.version.split()[0])
    if sys.version_info < (3, 7):
        print("✗ Python 3.7 or higher is required")
        return False
    return True

def test_ffmpeg():
    """Test if ffmpeg is available."""
    try:
        result = subprocess.run(["ffmpeg", "-version"], 
                              capture_output=True, text=True, check=True)
        version = result.stdout.split('\n')[0]
        print("✓ ffmpeg found:", version)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ ffmpeg not found. Please install ffmpeg.")
        return False

def test_ffprobe():
    """Test if ffprobe is available."""
    try:
        result = subprocess.run(["ffprobe", "-version"], 
                              capture_output=True, text=True, check=True)
        version = result.stdout.split('\n')[0]
        print("✓ ffprobe found:", version)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ ffprobe not found. Please install ffmpeg (includes ffprobe).")
        return False

def test_python_packages():
    """Test if required Python packages are installed."""
    required_packages = [
        ("whisper", "openai-whisper"),
        ("torch", "PyTorch"),
        ("numpy", "NumPy")
    ]
    
    all_installed = True
    for package, display_name in required_packages:
        try:
            __import__(package)
            print(f"✓ {display_name} installed")
        except ImportError:
            print(f"✗ {display_name} not installed")
            all_installed = False
    
    return all_installed

def main():
    """Run all tests."""
    print("Testing Video Transcriber Dependencies")
    print("=" * 40)
    
    tests = [
        test_python_version,
        test_ffmpeg,
        test_ffprobe,
        test_python_packages
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    if passed == total:
        print("🎉 All tests passed! Your environment is ready for video transcription.")
        print("\nYou can now run:")
        print("python video_transcriber.py /path/to/video/folder")
    else:
        print(f"❌ {total - passed} test(s) failed. Please fix the issues above.")
        print("\nCommon solutions:")
        print("1. Install ffmpeg: brew install ffmpeg (macOS) or sudo apt install ffmpeg (Ubuntu)")
        print("2. Install Python packages: pip install -r requirements.txt")

if __name__ == "__main__":
    main()
