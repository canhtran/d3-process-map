import json


def read_data(data_url):
	with open(data_url) as json_data:
		json = json.load(json_data)

	data = []
	errors = []

