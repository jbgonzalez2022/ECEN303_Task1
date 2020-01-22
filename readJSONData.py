import json

with open('identity.txt', 'r') as json_file:
	data = json.load(json_file)
	for student in data['students']:
		print('Name: ' + student['name'])
		print('GitHubID: ' + student['GitHubID'])
		print('NetID: ' + student['NetID'])
		print('')
