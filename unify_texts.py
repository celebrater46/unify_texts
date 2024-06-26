import os

DIR_PATH = "texts"

def get_filenames():
    file_names = [
        f for f in os.listdir(DIR_PATH) if os.path.isfile(os.path.join(DIR_PATH, f))
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
        tempstr += f"\n\n####################[PAGE_BREAK TITLE:{f}]####################\n\n"
        print(f"Added {f}")
    create_unified_text(tempstr)
    print(f"Created Unified.txt")

unify_texts()