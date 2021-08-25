import os
from Parse_Ts_File import ParseTsFile
import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt


class ProcessBatchFiles:
    def __init__(self, root):
        self.root_path = os.path.normpath(root)
        self.plain_graph = {}
        self.nx_graph = nx.DiGraph()
        self.all_import_files = {}

    def parse_batch_files_in_root(self):
        for rel_root, dirs, files in os.walk(self.root_path):
            if len(files) > 0:
                for f in files:
                    # print(f"{rel_root}, {dirs}, {files}")
                    abs_file = os.path.join(
                        os.path.normpath(rel_root), os.path.normpath(f))
                    if abs_file.split('.')[-1] == "ts":
                        parse_ts_file = ParseTsFile()
                        parse_ts_file.parse_file(abs_file)
                        self.all_import_files[os.path.relpath(abs_file, start=self.root_path).split('.')[0]] \
                            = [os.path.relpath(f, start=self.root_path) for f in parse_ts_file.import_files if
                               f[0] != '*'] + \
                              [f for f in parse_ts_file.import_files if f[0] == '*']

    def draw_graph_import_files(self):
        for host_path in self.all_import_files:
            self.nx_graph.add_node(host_path)
            for guest_path in self.all_import_files[host_path]:
                self.nx_graph.add_edge(guest_path, host_path)
        nt = Network('500px', '1000px', directed=True)
        nt.from_nx(self.nx_graph)
        nt.show('nx.html')
        # nx.draw(self.nx_graph, with_labels=True)
        # plt.show()


if __name__ == '__main__':
    pr = ProcessBatchFiles('C:\\FoxQuilt\\Development\\foxden-data-transfer\\src\\models')
    pr.parse_batch_files_in_root()
    pr.draw_graph_import_files()
