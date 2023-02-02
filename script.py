import os

# The directory where the videos are located
video_dir = "/directory"

# Read the titles from the text file
with open("titles.txt", "r") as file:
    titles = file.readlines()

# Remove newline characters from the titles
titles = [title.strip() for title in titles]
print(titles)

# Create a list of the video files in the directory
video_files = [file for file in os.listdir(video_dir) if file.endswith(".mp4")]


# Rename each video file with the corresponding title
for i, video_file in enumerate(video_files):
    old_path = os.path.join(video_dir, video_file)
    # print(old_path)
    new_title = f"{titles[i]}.mp4"
    new_path = os.path.join(video_dir, new_title)
    # print(new_path)
    os.rename(old_path, new_path)
