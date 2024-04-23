import os
import shutil
import ffmpeg

def create_output_folders(output_folder):
    
    mp3_folder = os.path.join(output_folder, "MP3")
    wma_folder = os.path.join(output_folder, "WMA")
    os.makedirs(mp3_folder, exist_ok=True)
    os.makedirs(wma_folder, exist_ok=True)
    return mp3_folder, wma_folder

def convert_wav_to_mp3(wav_file, output_folder):
    
    mp3_file = os.path.join(output_folder, os.path.splitext(os.path.basename(wav_file))[0] + '.mp3')

    
    (
        ffmpeg
        .input(wav_file)
        .output(mp3_file, ar=44100, ac=2, ab='192k')
        .run(overwrite_output=True)
    )

    print(f"Converted {wav_file} to {mp3_file}")

def convert_wav_to_wma(wav_file, output_folder):
    
    wma_file = os.path.join(output_folder, os.path.splitext(os.path.basename(wav_file))[0] + '.wma')

    
    (
        ffmpeg
        .input(wav_file)
        .output(wma_file)
        .run(overwrite_output=True)
    )

    print(f"Converted {wav_file} to {wma_file}")

def convert_wavs_in_folder(folder, output_folder):
    
    mp3_folder, wma_folder = create_output_folders(output_folder)

    
    for root, dirs, files in os.walk(folder):
        for file in files:
            
            if file.lower().endswith('.wav'):
                wav_file_path = os.path.join(root, file)
                try:
                    convert_wav_to_mp3(wav_file_path, mp3_folder)
                    convert_wav_to_wma(wav_file_path, wma_folder)
                except Exception as e:
                    print(f"Error processing {wav_file_path}: {e}")


directory = r'C:\Users\szymo\OneDrive\Pulpit\bu\data'


output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "converted")
os.makedirs(output_folder, exist_ok=True)  


convert_wavs_in_folder(directory, output_folder)
