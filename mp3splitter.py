from pydub import AudioSegment

def split_mp3(input_file, start_time, end_time, output_file):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(input_file)

    # Convert start_time and end_time to milliseconds
    start_ms = (int(start_time.split(':')[0]) * 60 + int(start_time.split(':')[1])) * 1000
    end_ms = (int(end_time.split(':')[0]) * 60 + int(end_time.split(':')[1])) * 1000
 
    # Slice the audio between start and end times
    sliced_audio = audio[start_ms:end_ms]

    # Export the sliced audio to a new MP3 file
    sliced_audio.export(output_file, format="mp3")

if __name__ == "__main__":
    input_file_path = input("Enter the path to your input MP3 file: ")
    start_time = input("Enter the start time in the format MM:SS: ")
    end_time = input("Enter the end time in the format MM:SS: ")
    output_file_path = input("Enter the path for the output sliced MP3 file: ")

    split_mp3(input_file_path, start_time, end_time, output_file_path)
