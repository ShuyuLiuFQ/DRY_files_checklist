import re
import os

def extract_path(line):
    return re.findall(r"'(.+)';$", line)[0]


def join_path(curr_abs_path, from_path):
    curr_abs_path = os.path.normpath(curr_abs_path)
    curr_abs_path_chunks = curr_abs_path.split('\\')
    from_path_chunks = from_path.split('/')
    if len(from_path_chunks) > 0 \
            and (from_path_chunks[0] == '.' or from_path_chunks[0] == '..'):
        del curr_abs_path_chunks[-1]
        if from_path_chunks[0] == '.':
            del from_path_chunks[0]
    elif len(from_path_chunks) > 0:
        return 'from npm_package'
    else:
        return None
    while len(from_path_chunks) > 0 and from_path_chunks[0] == '..':
        del curr_abs_path_chunks[-1]
        del from_path_chunks[0]
    # print(f"{curr_abs_path_chunks}, {from_path_chunks}")
    return '/'.join((curr_abs_path_chunks + from_path_chunks))