import os
import shutil

def organize_files(folder_path):
    # Get the list of files in the specified folder
    files = os.listdir(folder_path)

    # Create a dictionary to store files based on their first three words
    files_dict = {}

    for file in files:
        # Get the first three words of the file name
        first_three_words = ' '.join(file.split()[:3])

        # Check if the key already exists in the dictionary
        if first_three_words in files_dict:
            files_dict[first_three_words].append(file)
        else:
            files_dict[first_three_words] = [file]

    # Create Move folders and move files
    for key, value in files_dict.items():
        move_folder_path = os.path.join(folder_path, f"Move {key}")
        os.makedirs(move_folder_path, exist_ok=True)

        for file in value:
            current_file_path = os.path.join(folder_path, file)
            new_file_path = os.path.join(move_folder_path, file)
            shutil.move(current_file_path, new_file_path)

if __name__ == "__main__":
    folder_path = "D:/Pytho/convert video to mp3/extras/output_mp3"
    organize_files(folder_path)