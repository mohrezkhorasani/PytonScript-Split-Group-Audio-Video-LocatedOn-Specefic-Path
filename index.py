import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_folder):
    mp4_files = [filename for filename in os.listdir(input_folder) if filename.endswith(".mp4")]
    total_files = len(mp4_files)
    
    for i, filename in enumerate(mp4_files, start=1):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.splitext(input_path)[0] + ".mp3"
        
        video_clip = VideoFileClip(input_path)
        video_clip.audio.write_audiofile(output_path)
        
        percent_complete = (i / total_files) * 100
        files_left = total_files - i
        
        print(f"Conversion completed for {filename} - {percent_complete:.2f}% complete. {files_left} files left.")

if __name__ == "__main__":
    location = input("Enter the location of the MP4 files: ")
    convert_mp4_to_mp3(location)
