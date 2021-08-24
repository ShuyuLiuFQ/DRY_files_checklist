import re
import os


def extract_path(line):
    return re.findall(r"'(.+)';$", line)[0]


# curr_abs_path = C:\FoxQuilt\Development\foxden-policy-admin\src\models\mongodb\Application.ts
def join_path(curr_abs_path, from_path):
    curr_abs_path = os.path.normpath(curr_abs_path)
    curr_abs_path_chunks = curr_abs_path.split('\\')
    from_path_chunks = from_path.split('/')
    if len(from_path_chunks) > 0 \
            and (from_path_chunks[0] == '.' or from_path_chunks[0] == '..'):
        del curr_abs_path_chunks[-1]
        if from_path_chunks[0] == '.':
            del from_path_chunks[0]
    while len(from_path_chunks) > 0 and from_path_chunks[0] == '..':
        del curr_abs_path_chunks[-1]
        del from_path_chunks[0]
    # print(f"{curr_abs_path_chunks}, {from_path_chunks}")
    return '/'.join((curr_abs_path_chunks + from_path_chunks))


file = os.path.normpath("C:/FoxQuilt/Development/foxden-policy-admin/src/models/mongodb/Application.ts")

def generate_from_path(file):
    file = os.path.normpath(file)
    f = open(file)
    lines = f.readlines()

    i = 0
    in_import_flag = False
    while i < len(lines):
        curr_line = lines[i].strip()
        chunks = curr_line.split()
        if len(chunks) > 0 and chunks[0] == "import":
            in_import_flag = True
        if len(chunks) > 0 and in_import_flag:
            if curr_line[-1] == ';':
                in_import_flag = False
                from_path = extract_path(curr_line)
                new_path = join_path(file, from_path)
                print(new_path)
        elif len(chunks) > 0 and chunks[0] != "import" and in_import_flag is False:
            break
        i += 1
