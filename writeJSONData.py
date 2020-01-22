import json

data = {}
data['students'] = []
data['students'].append({
	'name': 'Joshua Gonzalez',
	'GitHubID': 'jbgonzalez2022',
	'NetID': '127007661'
})

with open('identity.txt', 'w') as outfile:
	json.dump(data, outfile)
