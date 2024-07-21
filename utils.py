import json


class Candidate:
    def __init__(self, path):
        self.path = path

    def load_candidates_in_dict(self):
        candidate = {}
        with open(self.path, 'r') as file:
            data = json.load(file)
        for i in data:
            candidate[i['id']] = i
        return candidate

    def get_data_from_x(self, id):
        candidate = {}
        with open(self.path, 'r') as file:
            data = json.load(file)
        for i in data:
            candidate[i['id']] = i
        return candidate[int(id)]
