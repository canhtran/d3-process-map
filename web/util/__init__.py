import json


def read_data(data_url):
    data = {}
    errors = []
    with open(data_url) as json_data:
        json_data = json.load(json_data)
    for obj in json_data:
        obj['dependedOnBy'] = []
        data[obj['name']] = obj
        for name in obj['depends']:
            if name in data:
                data[name]['dependedOnBy'].append(obj['name'])
            else:
                errors = errors.append(
                    "Unrecognized dependency: %s depends on %s" % (obj[name], name)
                )
    return data
    