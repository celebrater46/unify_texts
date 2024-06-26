import re

OUTPUT_DIL = "split"
UNIFIED_TXT = "unified.txt"

def get_lines():
    f = open(UNIFIED_TXT, "r", encoding='utf-8')
    lines = f.readlines()
    f.close()
    return lines

def get_title(txt):
    print(txt)
    re_obj = re.search(r'TITLE:[\w-]+.txt', txt)
    title = re_obj.group()
    title = title.replace("TITLE:", "")
    return title

def create_text(txt):
    # re_obj = re.search(r'TITLE:[\w-]+.txt', str)
    # title = re_obj.group()
    title = get_title(txt)
    tempstr = re.sub(r'#+[PAGE_BREAK TITLE:[\w-]+.txt]#+', '', txt)
    # print(re_obj.group())
    # print(title)
    f = open(f"{OUTPUT_DIL}/{title}", "w", encoding='utf-8')
    f.write(tempstr)
    f.close()

def create_texts(arr):
    for page in arr:
        create_text(page)

def split_text():
    lines = get_lines()
    pages = []
    tempstr = ""
    # print(lines)
    for line in lines:
        tempstr += line
        # tempstr = str(tempstr + line)
        if line.find("PAGE_BREAK") > -1:
            pages.append(tempstr)
            tempstr = ""     
    # print(tempstr)
    print(pages[5])
    # create_texts(pages)

def test(txt):
    # re_obj = re.search(r'TITLE:[\w-]+.txt', txt)
    re_obj = re.search(r'#+[PAGE_BREAK TITLE:[\w-]+.txt]#+', txt)
    print(re_obj.group())

# test("####################[PAGE_BREAK TITLE:20220104.txt]####################")
split_text()