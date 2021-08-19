import os
import pandas as pd


class FindFox:
    # servers_files = {servers_name1: {files}, servers_name2: {files}}
    def __init__(self, root_rep, servers_spe):
        self.root_repo = root_rep
        self.servers_spec = servers_spe
        self.servers_files = {}
        self.union_list = []

    def find_fox(self):
        union = set()
        for servers_name in self.servers_spec:
            servers_path = self.root_repo + '\\' + servers_name + '\\' + "src"
            files_list = []
            for rel_root, dirs, files in os.walk(servers_path):
                rel_path = os.path.relpath(rel_root, start=servers_path)
                root_split_list = rel_path.split('\\')
                if len(root_split_list) > 0 and root_split_list[0] in self.servers_spec[servers_name]:
                    file_list = [rel_path + '\\' + f for f in files if f.split('.')[-1] == "ts"]
                    files_list += file_list
            files_set = set(files_list)
            union = union.union(files_set)
            self.servers_files[servers_name] = files_set
        self.union_list = sorted(list(union))
        print(len(self.union_list))

    def print_report(self, csv_path='report.csv'):
        data = {
            'models': self.union_list
        }
        column_names = ['models']
        for servers_name in self.servers_files:
            one_hot = [1 if file in self.servers_files[servers_name] else 0
                       for file in self.union_list]
            column_names.append(servers_name)
            data[servers_name] = one_hot
        df = pd.DataFrame(data, columns=column_names)
        df.to_csv(csv_path)

    def union_files(self):
        pass


if __name__ == '__main__':
    root_repo = "C:\\FoxQuilt\\Development"
    servers_spec = {
        "foxcom-forms-backend": ['models', 'utils'],
        "foxcom-payment-backend": ['models', 'utils'],
        "foxden-policy-document-backend": ['models', 'utils'],
        "foxden-billing": ['models', 'utils'],
        "foxden-policy-admin": ['models', 'utils'],
        "foxden-data-transfer": ['models', 'utils'],
    }
    fox = FindFox(root_repo, servers_spec)
    fox.find_fox()
    fox.print_report()
