import csv
import json

def strip_spotify_id(spotify_id):
	return spotify_id.split(':')[2]

'''
Returns uqunique list of tags.
If there are multiple tags of the same name, the onw with highest rating is preserved.
'''
def uniqy_tags(tags):
	tags_uq = {}
	for tag in tags:
		tag_name = tag['tag'].strip() 
		if not tag_name in tags_uq or tags_uq[tag_name]['count'] < tag['count']:
			tags_uq[tag_name] = tag
	return list(tags_uq.values())

with open('../data/tags.jl', encoding='utf8') as in_file, \
		open('../data/csv/tags.csv', 'a', encoding='utf8') as out_file:
	out_file.write('"song_spotify_id","genre","tag","popularity"\n')
	writer = csv.writer(out_file, delimiter=";", lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
	for json_line in in_file:
		line = json.loads(json_line)
		spotify_id = line['uri_id'].split(':')[2]
		for tag in uniqy_tags(line['tags']):
			writer.writerow(list(map(lambda x: x.strip(), [
				strip_spotify_id(line['uri_id']),
				line['genre'],
				tag['tag'],
				str(tag['count']),
			])))
