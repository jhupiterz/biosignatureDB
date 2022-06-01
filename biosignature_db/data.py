import json

def read_json_data(json_file):
    with open(json_file, 'r') as myfile:
        data=myfile.read()
    research = json.loads(data)
    return research

def read_all_json_files():
    file_paths = ['data/research.json', 'data/researcher.json',
                  'data/biosignature.json', 'data/environment.json']
    json_list = []
    for file in file_paths:
        json_list.append(read_json_data(file))
    return json_list

def read_all_json_files_jupyter():
    file_paths = ['../biosignature_db/data/publication.json', '../biosignature_db/data/author.json',
                  '../biosignature_db/data/biosignature.json', '../biosignature_db/data/environment.json']
    json_list = []
    for file in file_paths:
        json_list.append(read_json_data(file))
    return json_list