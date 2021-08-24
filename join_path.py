import os


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


curr_abs_path1 = "C:\FoxQuilt\Development\foxden-policy-admin\src\models\mongodb\Application.ts"
from_path1 = "../../this"
print(join_path(curr_abs_path1, from_path1))
