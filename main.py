import os

def rename_png_files(directory):
    counter = 0
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            file_path = os.path.join(directory, filename)
            new_filename = str(counter) + ".png"  # Yeni dosya adı için numaralandırma
            new_file_path = os.path.join(directory, new_filename)
            os.rename(file_path, new_file_path)
            counter += 1

# Dosya yolunu belirtin
directory_path = input("Directory path: ")
rename_png_files(directory_path)