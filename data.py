import json


def read_data():
    with open('static\data\PetDataSet.json') as file:
        data = json.load(file)
        return data
