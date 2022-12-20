
# File Sorter V1

This Python script sorts files in a specified directory into subdirectories based on their file extension.
Usage


## Usage/Examples

1. Update the source_dir variable to specify the directory where the files are located.
2. Update the directory variables (e.g. image_dir, video_dir, doc_dir, etc.) to specify the directories where the files should be moved.
3. Run the script.
```
#File Extension Mapping
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
