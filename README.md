File Sorter
This Python script sorts files in a specified directory into subdirectories based on their file extension.
Usage
Update the source_dir variable to specify the directory where the files are located.
Update the directory variables (e.g. image_dir, video_dir, doc_dir, etc.) to specify the directories where the files should be moved.
Run the script.

File Extension Mapping
The script sorts files into the following directories based on their file extension:
Images: .jpg, .png, .gif, .jpeg
Compressed: .zip, .rar, .7z
Videos: .mp4, .avi, .mkv
Documents: .doc, .docx, .pdf, .xlsx, .xls, .pptx, .ppt, .potx, .csv, .odt, .xlsm, .rtf
Music: .mp3, .wav
PSD: .psd
AI: .ai, .svg
Torrent: .torrent
HTML: .html, .htm
EPUB: .epub
Fonts: .ttf
Text: .txt
Files with unknown extensions will be skipped.
Note

If a file with the same name already exists in the destination directory, the script will generate a new name for the file by appending a number in parentheses to the filename. For example, if a file named "example.jpg" already exists in the destination directory, the script will move the new file as "example (1).jpg". If a file named "example (1).jpg" already exists, the script will move the new file as "example (2).jpg", and so on.
