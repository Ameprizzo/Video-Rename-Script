# Video Rename Script

This script renames videos in a specified directory based on a list of titles in a text file.
Usage

    Put the script in the same directory as the text file containing the titles.
    Make sure that the text file is formatted correctly, with each title on a separate line.
    Specify the directory containing the videos in the video_dir variable in the script.
    Run the script using a Python interpreter.

### Requirements

    Python 3
    The videos and the text file must be in the same directory as the script, or the video_dir variable must be updated to reflect the correct location of the videos.

### Notes

    The script assumes that the video files are .mp4 files. If your video files have a different extension, you will need to update the video_files line in the script to match the correct extension.
    . The script renames the videos in the order they appear in the text file. If the titles in the text file do not match the order of the video files in the directory, the resulting video names will be incorrect.