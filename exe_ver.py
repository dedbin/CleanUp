import os
import shutil
import zipfile
import re


def del_dup_main():
    def remove_duplicates(directory):
        for root, dirs, files in os.walk(directory):
            filedict = {}
            for filename in files:
                filepath = os.path.join(root, filename)

                match = re.search(r'^(.*?)\((\d+)\)(\.[^.]*)?$', filename)
                if match:
                    name = match.group(1)
                    num = int(match.group(2))
                    ext = match.group(3) or ''

                    if name not in filedict:
                        filedict[name] = [(num, filepath, ext)]
                    else:
                        filedict[name].append((num, filepath, ext))
            for name in filedict:
                files = filedict[name]
                files.sort(key=lambda x: x[0])
                print(files)
                latest = files[-1][1]
                ext = files[-1][2]

                for number, filepath, _ in files[:-1]:
                    print(f"дубликат удален: {filepath}")
                    os.remove(filepath)

                os.rename(latest, os.path.join(root, f"{name}{ext}"))
                print(f"переимеован {latest} в {name}{ext}")

    remove_duplicates(os.path.expanduser("~/Downloads"))


def del_temp_main():
    temp_directories = [
        '/private/var/folders',
        '~/Library/Caches',
        '~/Library/Logs',
        '~/Downloads',
        '~/Desktop'
    ]

    extensions = [
        '.log',
        '.cache',
        '.tmp',
        '.dmg',
        '.pkg'
    ]

    for directory in temp_directories:
        for dirpath, dirnames, filenames in os.walk(os.path.expanduser(directory)):
            for filename in filenames:
                if os.path.splitext(filename)[1].lower() in extensions:
                    filepath = os.path.join(dirpath, filename)
                    try:
                        if os.path.isfile(filepath):
                            os.remove(filepath)
                        elif os.path.isdir(filepath):
                            shutil.rmtree(filepath)
                        print(f"удален {filepath}")
                    except Exception as e:
                        print(f"ошибка при удалении {filepath}: {e}")

        if directory == '~/OneDrive/Desktop':
            desktop_path = os.path.expanduser(directory)
            screenshot_files = [f for f in os.listdir(desktop_path) if f.startswith('Screenshot')]
            for file in screenshot_files:
                filepath = os.path.join(desktop_path, file)
                try:
                    os.remove(filepath)
                    print(f"удален {filepath}")
                except Exception as e:
                    print(f"ошибка при удалении {filepath}: {e}")


def down_main():
    downloads_dir = os.path.expanduser("~/Downloads")

    file_types = {
        "Image": [".jpg", ".jpeg", ".png", ".gif", ".tiff", ".bmp", ".eps"],
        "Code": [".ipynb", ".py", ".js", ".html", ".css", ".php", ".cpp", ".h", ".java"],
        "Document": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Audio": [".mp3", ".wav", ".aac", ".ogg", ".oga"],
        "Video": [".mp4", ".avi", ".mov", ".flv", ".wmv", ".mpeg"],
        "Photoshop": [".psd"],
        "Applications": [".exe", ".dmg", ".pkg"],
    }

    for folder_name in file_types.keys():
        folder_path = os.path.join(downloads_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for filename in os.listdir(downloads_dir):
        filepath = os.path.join(downloads_dir, filename)

        if filename.endswith(".zip"):
            unzip_dir = os.path.join(downloads_dir, filename[:-4])
            if not os.path.exists(unzip_dir):
                with zipfile.ZipFile(filepath, 'r') as zip_ref:
                    zip_ref.extractall(downloads_dir)
            os.remove(filepath)
            print(f"распакован и удален {filename}")

        elif filename.endswith(".torrent"):
            os.remove(filepath)
            print(f"удален {filename}")

        elif filename.endswith(".srt"):
            dest_folder = os.path.join(downloads_dir, "Video", ".subtitle")
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            shutil.move(filepath, os.path.join(dest_folder, filename))
            print(f"перемещен {filename} в {dest_folder}")

        else:
            for folder_name, extensions in file_types.items():
                if any(filename.endswith(ext) for ext in extensions):
                    dest_folder = os.path.join(downloads_dir, folder_name)
                    shutil.move(filepath, os.path.join(dest_folder, filename))
                    print(f"перемещен {filename} в {dest_folder}")
                    break


del_temp_main()
del_dup_main()
down_main()
