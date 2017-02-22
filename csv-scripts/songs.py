import csv
import json

def strip_spotify_id(spotify_id):
	return spotify_id.split(':')[2]

with open('../data/songs.jl', encoding='utf8') as in_file, \
		open('../data/csv/songs.csv', 'a', encoding='utf8') as out_file:
	out_file.write('"spotify_id","name","artist","position","genre_name"\n')
	writer = csv.writer(out_file, delimiter=";", lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
	for json_line in in_file:
		line = json.loads(json_line)
		for song in line['songs']:
			writer.writerow(list(map(lambda x: x.strip(), [
				strip_spotify_id(song['uri_id']),
				song['name'],
				song['artist'],
				song['position'],
				line['genre']
			])))
