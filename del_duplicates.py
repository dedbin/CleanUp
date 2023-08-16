import os
import re


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
