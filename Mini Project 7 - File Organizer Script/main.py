import os
import shutil

def organize_folder(folder_path):
    ## Flow Summary (Algorithm):
    # 1. List all files/folders in the folder
    #    Function: os.listdir(folder_path)
    # 2. Create full path for each item
    #    Function: os.path.join(folder_path, filename)
    # 3. Check if item is a file
    #    Function: os.path.isfile(file_path)
    # 4. Get file extension
    #    Function: os.path.splitext(filename), ext.lower()
    # 5. Find which category folder it belongs to
    #    Function: dict.items()
    # 6. Create target folder if not exists
    #    Function: os.makedirs(target_folder, exist_ok=True)
    # 7. Move file to target folder
    #    Function: shutil.move(file_path, target_folder)
    # 8. Break the loop once moved
    #    Statement: break

    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.ppt', '.csv', '.odt'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv', '.webm'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2'],
        'Scripts': ['.py', '.js', '.sh', '.bat', '.rb', '.pl', '.php'],
        'Fonts': ['.ttf', '.otf', '.woff', '.woff2'],
        'Data': ['.json', '.xml', '.yaml', '.yml', '.db', '.sql'],
        'Executables': ['.exe', '.msi', '.apk', '.bin', '.app', '.jar'],
        'Web': ['.html', '.css', '.php', '.jsp', '.asp'],
        'Config': ['.ini', '.cfg', '.conf', '.env'],
        'Java': ['.java', '.class', '.jar', '.pom'],   # Java source, compiled, package, project file
        'Jupyter': ['.ipynb']  # Jupyter notebook
    }

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()
            
            for folder, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    break
    print("Successfully done")

path = "your directory path"
# Example usage
organize_folder(path)
