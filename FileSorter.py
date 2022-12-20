#This Python script sorts files in a specified directory into subdirectories based on their file extension.
import os
import shutil

# Specify the directory where the files are located
source_dir = "C:\\Users\\Username\\Downloads"

# Specify the directories where the files should be moved
image_dir = "C:\\Users\\Username\\Downloads\\Images"
video_dir = "C:\\Users\\Username\\Downloads\\Videos"
doc_dir = "C:\\Users\\Username\\Downloads\\Documents"
music_dir = "C:\\Users\\Username\\Downloads\\Music"
psd_dir = "C:\\Users\\Username\\Downloads\\PSD"
ai_dir = "C:\\Users\\Username\\Downloads\\AI"
html_dir = "C:\\Users\\Username\\Downloads\\HTML"
zip_dir = "C:\\Users\\Username\\Downloads\\Compressed"
epub_dir = "C:\\Users\\Username\\Downloads\\EPUB"
torrent_dir = "C:\\Users\\Username\\Downloads\\Torrent"
fonts_dir = "C:\\Users\\Username\\Downloads\\Fonts"
txt_dir = "C:\\Users\\Username\\Downloads\\Text"

# Loop through all files in the source directory
for filename in os.listdir(source_dir):
    # Get the file extension
    extension = os.path.splitext(filename)[1]

    # Determine the destination directory based on the file extension
    if extension in (".jpg", ".png", ".gif", ".jpeg"):
        dest_dir = image_dir
    elif extension in (".zip", ".rar", ".7z"):
        dest_dir = zip_dir
    elif extension in (".mp4", ".avi", ".mkv"):
        dest_dir = video_dir
    elif extension in (".doc", ".docx", ".pdf", ".xlsx", ".xls", ".pptx", ".ppt", ".potx", ".csv", ".odt", ".xlsm", ".rtf"):
        dest_dir = doc_dir
    elif extension in (".mp3", ".wav"):
        dest_dir = music_dir
    elif extension == ".psd":
        dest_dir = psd_dir
    elif extension in (".ai", ".svg"):
        dest_dir = ai_dir
    elif extension == ".torrent":
        dest_dir = torrent_dir
    elif extension in (".html", ".htm"):
        dest_dir = html_dir
    elif extension == ".epub":
        dest_dir = epub_dir
    elif extension == ".ttf":
        dest_dir = fonts_dir
    elif extension == ".txt":
        dest_dir = txt_dir
    else:
        # Skip files with unknown extensions
        continue

    # Construct the full path to the destination file
    dest_path = os.path.join(dest_dir, filename)

    # Check if the destination file already exists
    if os.path.exists(dest_path):
        # Generate a new name for the file
        i = 1
        while True:
            new_filename = f"{os.path.splitext(filename)[0]} ({i}){extension}"
            new_dest_path = os.path.join(dest_dir, new_filename)
            if not os.path.exists(new_dest_path):
                break
            i += 1

        # Update the destination path with the new filename
        dest_path = new_dest_path

    # Move the file to the destination directory
    shutil.move(os.path.join(source_dir, filename), dest_path)
