import json
import os
import pandas as pd
import psycopg2

DATABASE_CREDENTIALS = {
    "HOST": os.environ.get('HOST'),
    "DATABASE": os.environ.get('DATABASE'),
    "USER": os.environ.get('USER'),
    "DB_PASSWORD": os.environ.get('DB_PASSWORD')
}

def read_database():
    conn = psycopg2.connect(
    host=DATABASE_CREDENTIALS['HOST'],
    database=DATABASE_CREDENTIALS['DATABASE'],
    user=DATABASE_CREDENTIALS['USER'],
    password=DATABASE_CREDENTIALS['DB_PASSWORD'])
    cur = conn.cursor()
    cur.execute('SELECT * FROM biosignature')
    results = cur.fetchall()
    column_names = ['biosignature_id', 'biosignature_cat', 'biosignature_subcat',
                    'biosignature_name', 'indicative_of', 'detection_methods',
                    'sample_type', 'sample_subtype', 'number_of_samples', 'min_age',
                    'max_age', 'env_conditions', 'paleoenvironment', 'location_name',
                    'latitude', 'longitude', 'mars_counterpart', 'mars_latitude',
                    'mars_longitude', 'pub_ref', 'pub_url', 'status']
    df = pd.DataFrame(results, columns=column_names)
    return df

def update_validated_data(bio_id):
    conn = psycopg2.connect(
        host=DATABASE_CREDENTIALS['HOST'],
        database=DATABASE_CREDENTIALS['DATABASE'],
        user=DATABASE_CREDENTIALS['USER'],
        password=DATABASE_CREDENTIALS['DB_PASSWORD'])
    cur = conn.cursor()
    query = """UPDATE biosignature
               SET status = ' 🟢 validated'
               WHERE biosignature_id = %s"""
    cur.execute(query, (bio_id,))
    conn.commit()
    cur.close()
    conn.close()

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