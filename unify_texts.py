import os

def get_filenames():
    dir_path = "texts"
    file_names = [
        f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))
    ]
    return file_names

def get_text(file_name):
    f = open(f"texts/{file_name}", "r", encoding='utf-8')
    text = f.read()
    f.close()
    return text

def create_unified_text(txt):
    f = open("unified.txt", "w", encoding='utf-8')
    f.write(txt)
    f.close()

def unify_texts():
    tempstr = ""
    fs = get_filenames()
    for f in fs:
        tempstr += get_text(f)
        tempstr += "\n\n####################[PAGE_BREAK]####################\n\n"
    create_unified_text(tempstr)

unify_texts()