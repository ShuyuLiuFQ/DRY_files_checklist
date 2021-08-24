import os
from Helper import extract_path, join_path
import networkx as nx
import matplotlib.pyplot as plt


class FoxGraph():

    def __init__(self, root_path=None):
        self.root_path = os.path.normpath(root_path)
        self.plain_graph = {}
        self.graph = nx.DiGraph()

    def generate_one_plain_graph(self, file_abs_path):
        file = os.path.normpath(file_abs_path)
        file_abs_name = file.split('.')[0]
        # print(f"{file}, {file_abs_name}")
        file_rel_name = os.path.relpath(file_abs_name, start=self.root_path)
        self.plain_graph[file_rel_name] = set()
        f = open(file)
        lines = f.readlines()
        i = 0
        in_import_flag = False
        while i < len(lines):
            curr_line = lines[i].strip()
            chunks = curr_line.split()
            if len(chunks) > 0 and chunks[0] == "//":
                i += 1
                continue
            if len(chunks) > 0 and chunks[0] == "import":
                in_import_flag = True
            if len(chunks) > 0 and in_import_flag:
                if curr_line[-1] == ';':
                    in_import_flag = False
                    from_path = extract_path(curr_line)
                    new_abs_path = os.path.normpath(join_path(file, from_path))
                    new_rel_path = os.path.relpath(new_abs_path, start=self.root_path)
                    self.plain_graph[file_rel_name].add(new_rel_path)
            elif len(chunks) > 0 and chunks[0] != "import" and in_import_flag is False:
                break
            i += 1

    def generate_plain_graph(self):
        for rel_root, dirs, files in os.walk(self.root_path):
            if len(files) > 0:
                for f in files:
                    # print(f"{rel_root}, {dirs}, {files}")
                    abs_files = os.path.join(os.path.normpath(rel_root), os.path.normpath(f))
                    if abs_files.split('.')[-1] == "ts":
                        self.generate_one_plain_graph(abs_files)

    def draw_graph(self):
        for host_path in self.plain_graph:
            self.graph.add_node(host_path, colorsys="red")
            for guest_path in self.plain_graph[host_path]:
                self.graph.add_edge(guest_path, host_path)
        nx.draw(self.graph, with_labels=True)
        plt.show()



if __name__ == '__main__':
    fox1 = FoxGraph("C:/FoxQuilt/Development/foxden-policy-admin/src/models/mongodb")
    fox1.generate_plain_graph()
    fox1.draw_graph()
    # fox2 = FoxGraph("C:/FoxQuilt/Development/foxcom-forms-backend/src/context")
    # fox2.generate_plain_graph()
    # fox2.draw_graph()
    # print(fox.plain_graph['index'])

