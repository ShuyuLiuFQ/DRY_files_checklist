import re
import os
from Helper import join_path, extract_path


# one file once a time
class ParseTsFile:
    def __init__(self):
        self.flags = {
            "import": False,
        }
        self.parser = {
            "import": self.import_parser,
        }
        self.import_files = []
        self.curr_line = ""
        self.temp_content = []

    # check which flag is set, if None, return None
    def recognize_flags(self):
        for key in self.flags:
            if self.flags[key]:
                return key
        return None

    # figure out which flag need to be set
    def identifier(self, file):
        curr_line = self.curr_line.strip()
        chunks = curr_line.split()
        if len(chunks) == 0:
            return
        if chunks[0] == "import":
            self.flags["import"] = True
            self.import_parser(file)
            return

    def import_parser(self, file):
        chunks = self.curr_line.strip().split()
        self.temp_content += [re.sub('[{},]', '', c) for c in chunks if re.sub('[{},]', '', c) != '']
        if self.curr_line.strip()[-1] == ';':
            self.flags["import"] = False
            # print(self.temp_content)
            # extract path
            from_path = extract_path(self.temp_content[-1])
            new_abs_path = os.path.normpath(
                join_path(file, from_path))
            # if new_abs_path[0] != '@':
            #     new_rel_path = os.path.relpath(new_abs_path, start=self.root)
            # else:
            #     new_rel_path = new_abs_path
            self.import_files.append(new_abs_path)
            self.temp_content = []
        return

    # parse file line by line
    # if the flag hasn't been set, identify the line to set the flag
    # if the flag has been set, feed the file to the parser accordingly
    def parse_file(self, abs_file_path):
        file = os.path.normpath(abs_file_path)
        f = open(file)
        lines = f.readlines()
        for line in lines:
            self.curr_line = line
            flag = self.recognize_flags()
            # no flag is set
            if flag is None:
                self.identifier(file)
            else:
                self.parser[flag](file)


if __name__ == '__main__':
    p = ParseTsFile()
    p.parse_file('C:\\FoxQuilt\\Development\\foxden-data-transfer\\src\\sentry.ts')
    print(p.import_files)
