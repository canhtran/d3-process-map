import json


def read_data(data_url):
	data = {}
	errors = []
	with open(data_url) as json_data:
		json_data = json.load(json_data)
	for obj in json_data:
		obj['dependedOnBy'] = []
		data[obj['name']] = obj

	for obj in json_data:
		for name in obj['depends']:
			if name in data:
				data[name]['dependedOnBy'].append(obj['name'])
			else:
				errors.append(
					"Unrecognized dependency: %s depends on %s" % (obj['name'], name)
				)
			print(name)
	return data, errors


def read_config(config_url):
	with open(config_url) as data:
		configurate = json.load(data)
	configurate['jsonUrl'] = '/jsonurl'
	return configurate
